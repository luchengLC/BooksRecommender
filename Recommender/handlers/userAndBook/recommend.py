from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package
import operator
from collections import OrderedDict
import random


''' 
    TO DO
    三条线程
    分别处理
    标签推荐
    item cf 书籍推荐
    基于内容 书籍推荐
'''



#  标签推荐
#  TO DO
#  少了 时间 的权重
@require_http_methods(["POST"])
def handle_recommend_tags(request):
    userId = request.POST.get('userId')
    res = deal_recommend_tags(userId)
    # 随机取
    if len(res) >= 10:
        ress = random.sample(res, 10)
    else:
        ress = random.sample(res, len(res))
    for i in ress:
        print(i['weight'], '****', i['tagName'])
    return JsonResponse(package.successPack(ress))


#  标签搜索
@require_http_methods(["GET"])
def handle_recommend_tags_search(request):
    wd = request.GET.get('wd')
    pageno = int(request.GET.get('pageno'))

    # 求对应列表
    count = (pageno - 1) * 20  # 用于辅助翻页
    sql_base = 'FROM br_tags LEFT JOIN br_books ON br_tags.bookId = br_books.bookId WHERE br_tags.tagName = %s ORDER BY ratingScore DESC '
    sql = 'SELECT br_tags.bookId, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary ' + sql_base + ' LIMIT ' + str(
        count) + ',20;'
    lists = []  # 返回的参数列表
    result_code, lists = dbOptions.search(sql, wd)

    sql_count = 'SELECT COUNT(br_tags.bookId) AS num ' + sql_base
    counts = int(dbOptions.search_count(sql_count, wd))  # 查询到对应的总数
    page_count = math.ceil(counts / 20)  # python3:/是精确除，然后向上取整。每页20

    # 给每本书 查找 tags
    for i in range(len(lists)):
        sql_tag = 'SELECT tagName, bookTagRank FROM br_tags WHERE bookId = %s ORDER BY bookTagRank'
        result_tags_code, result_tags = dbOptions.tag_query(sql_tag, lists[i]['bookId'])
        if result_tags_code == 0:
            lists[i]['tags'] = result_tags

    if result_code == 0:
        data = {
            'page_count': page_count,
            'list': lists
        }
        return JsonResponse(package.successPack(data))
    else:
        return JsonResponse(package.errorPack(lists[0]))


def deal_recommend_tags(userId):
    sql = 'SELECT favor.bookId, bookName,starNum, ratingScore, ratingNum, bookTagRank, tagName FROM favor, br_books, br_tags WHERE favor.userId = %s AND br_books.bookId = favor.bookId AND br_tags.bookId = favor.bookId ORDER BY bookId, bookTagRank'
    result_code, result = dbOptions.favor_list_query(sql, userId)

    # 算法
    list = []
    res = []
    # 喜爱列表为空
    if len(result) == 0:
        return res

    for i in range(len(result)):
        tmp = {
            'starNum': int(result[i][2]),
            'ratingScore': float(result[i][3]),
            'ratingNum': int(result[i][4]),
            'bookTagRank': int(result[i][5]),
            'tagName': result[i][6]
        }
        list.append(tmp)

    for i in range(len(list)):
        # 计算权重
        list[i]['weight'] = list[i]['starNum'] / 1.8 * (10 - list[i]['bookTagRank']) / 10 * math.log(
            list[i]['ratingNum'], 10.0) * list[i]['ratingScore'] / 10

    # 排序
    list.sort(key=lambda k: (k.get('weight', 0)), reverse=True)

    # 去重
    b = OrderedDict()
    for item in list:
        b.setdefault(item['tagName'], {**item, 'freq': 0})['freq'] += 1

    for k, v in b.items():
        print(v['weight'], ' ==== ', v['tagName'])
        tmp = {
            'tagName': v['tagName'],
            'weight': v['weight'],
            'freq': v['freq'],
        }
        res.append(tmp)
    # 返回 前20个 标签
    if len(res) >= 20:
        return res[:20]
    else:
        return res


# 基于物品的协同过滤
# 结合
# 基于内容推荐算法
@require_http_methods(["POST"])
def handle_recommend_books(request):
    userId = request.POST.get('userId')
    sql = 'SELECT userId, bookId, starNum FROM favor'
    result_code, result = dbOptions.favor_all_query(sql, userId)

    # if result_code == 0:
    res = preDeal(result)
    W = itemSimilarity(res)
    ress = CFRecommend(res, userId, W)

    # 到数据库去查询被推荐的书籍信息
    rec_sql = 'SELECT bookId, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary FROM br_books WHERE bookId = %s'
    rec_code, rec_res = dbOptions.cf_rec_query(rec_sql, ress)
    if rec_code == 0:
        list = {
            'list': rec_res
        }
        return JsonResponse(package.successPack(list))
    else:
        return JsonResponse(package.errorPack(rec_res))


# 预处理 数据格式
def preDeal(result):
    res = dict()
    for i in result:
        res.setdefault(i[0], {})
        res[i[0]][i[1]] = int(i[2])
    return res


# 计算 itemCF的相似度矩阵
def itemSimilarity(train):
    C = dict()
    N = dict()
    # 计算出 同现矩阵，并且惩罚热门
    for user, items in train.items():
        for i in items.keys():
            N.setdefault(i, 0)
            N[i] += 1
            C.setdefault(i, {})
            for j in items.keys():
                if i == j:
                    continue
                C[i].setdefault(j, 0)
                C[i][j] += 1 / math.log(1 + len(items) * 1.0)
    # print('****************************')
    # print(C)
    # print('****************************')

    # 每个矩阵我的值 除以 根号（N[i]*N[j]）,归一化，相当于求余弦相似度
    W = dict()
    for i, related_items in C.items():
        W.setdefault(i, {})
        for j, cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    # print('============================================')
    # print(W)
    # print('============================================')
    return W


# 根据表推荐
# 需要修改 ==== 做成，把item cf 相似度存在数据库中
# 根据用户的好评，再做计算
def CFRecommend(train, user, W, K=8, N=10):
    # K ======= 取最相近的 3个用户的数据
    # N ======= 乘完评分矩阵后 取 TOP N
    rank = dict()
    action_item = train[user]
    for item, score in action_item.items():
        for j, wj in sorted(W[item].items(), key=lambda x: x[1], reverse=True)[0:K]:
            if j in action_item.keys():
                continue
            rank.setdefault(j, 0)
            # 乘以 评分矩阵 用for一个个乘
            rank[j] += score * wj
            # 乘完评分矩阵之后，再排序取最佳的
    return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])
    # return dict(rank)
