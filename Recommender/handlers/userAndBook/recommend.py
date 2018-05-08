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


#  标签推荐
#  啊啊啊啊啊，用什么 算法
@require_http_methods(["POST"])
def handle_recommend_tags(request):
    userId = request.POST.get('userId')
    res = deal_recommend_tags(userId)
    # 随机取
    ress = random.sample(res, 10)
    return JsonResponse(package.successPack(ress))


# 标签搜索
@require_http_methods(["GET"])
def handle_recommend_tags_search(request):
    wd = request.GET.get('wd')
    pageno = int(request.GET.get('pageno'))

    # 求对应列表
    count = (pageno - 1) * 20  # 用于辅助翻页
    sql_base = 'FROM br_tags LEFT JOIN br_books ON br_tags.bookId = br_books.bookId WHERE br_tags.tagName = %s ORDER BY ratingScore DESC '
    sql = 'SELECT br_tags.bookId, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary '+ sql_base + ' LIMIT '+str(count)+',20;'
    lists = []  # 返回的参数列表
    result_code, lists = dbOptions.search(sql, wd)


    sql_count = 'SELECT COUNT(br_tags.bookId) AS num '+sql_base
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


#  啊啊啊啊啊，用什么 算法
@require_http_methods(["GET"])
def handle_recommend_books(request):
    pass


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
        list[i]['weight'] = list[i]['starNum'] / 2.5 + (10 - list[i]['bookTagRank']) / 10 * math.log(
            list[i]['ratingNum'], 2.0) * list[i]['ratingScore'] / 10

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
    # 返回 前18个 标签
    if len(res) >= 18:
        return res[:18]
    else:
        return res
