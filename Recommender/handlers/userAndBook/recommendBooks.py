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
import threading




''' 
    TO DO
    三条线程
    分别处理
    标签推荐              TO DO：1. 时间权重的处理   2. 多选
    item cf 书籍推荐      TO DO：1. 推荐原因，需要； 2.存储在数据库，设计每天更新一次  3.时间权重的处理
'''


@require_http_methods(["POST"])
def handle_recommend_books(request):
    """
    书籍推荐 接口
    基于物品的协同过滤 结合 基于内容推荐算法
    :param request: request
    :return: 
    """

    userId = request.POST.get('userId')

    # 查找用户的喜爱列表  已按时间和喜爱度排序
    user_favor_sql = 'SELECT bookId, starNum FROM favor WHERE userId = %s ORDER BY starTime DESC, starNum DESC '
    result_favor_sql_code, favor_list = dbOptions.cf_query_user_favor(user_favor_sql, userId)

    # 创建新线程 2个 分别进行两种推荐
    threadCf = cfThread(userId, favor_list, 'cfThread')
    threadCont = contentThread(userId, favor_list, 'contentThread')

    # 开启新线程
    threadCf.start()
    threadCont.start()
    # 等待线程完成
    threadCf.join()
    threadCont.join()

    # 获取结果
    contResult = threadCont.get_result()
    cfResult = threadCf.get_result()

    lenCF = len(cfResult)
    lenCont = len(contResult)

    if lenCF >= 6 and lenCont >= 6:
        res = random.sample(cfResult[0:6] + contResult[0:6], 12)
    elif lenCF >= 6 > lenCont:
        res = random.sample(cfResult[0:6] + contResult, 6 + lenCont)
    elif lenCF < 6 <= lenCont:
        res = random.sample(cfResult + contResult[0:6], 6 + lenCF)
    else:
        res = random.sample(cfResult + contResult, lenCF + lenCont)

    list = {
        'list': res
    }

    return JsonResponse(package.successPack(list))


def dealItemCFRecommend():
    """
    item cf 定时处理
    :return: 
    """
    # print('==================== 现在正在执行 ==================')
    sql = 'SELECT userId, bookId, starNum FROM favor'
    result_code, result = dbOptions.favor_all_query(sql)

    if result_code == 0:
        res = preDeal(result)
        W = itemSimilarity(res)

    # 直接从数据库 表cf_similar 中取userId 喜爱列表里面的最相似TOP 15
    pass


def preDeal(result):
    """
    cf 预处理 数据格式
    :param result: 
    :return: 
    """
    res = dict()
    for i in result:
        res.setdefault(i[0], {})
        res[i[0]][i[1]] = int(i[2])
    return res


def itemSimilarity(train):
    """
    计算 itemCF的相似度矩阵
    :param train: 
    :return: 
    """
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

    # 每个矩阵我的值 除以 根号（N[i]*N[j]）,归一化，相当于求余弦相似度
    W = dict()
    list = []
    for i, related_items in C.items():
        W.setdefault(i, {})
        for j, cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])

            tmp = {
                'bookId1': i,
                'bookId2': j,
                'similar': W[i][j]
            }
            list.append(tmp)

    # 这里可以把值插入表cf_similar， Yeah，么么哒
    dbOptions.cf_insert_update(list)
    return W


def cfRecommend(userId, favor_list, K=8, N=30):
    """
    基于物品的协同过滤推荐 item-cf 的即时处理
    :param userId:
    :param K: 
    :param N: 
    :return: 
    """

    # 根据 时间 和 喜爱度排序，取前K个，
    favor_sql_result_topK = favor_list[0:K]

    # 把该用户已评价过的书籍id集中起来，便于一会儿的过滤
    user_favor = []
    for i in favor_list:
        user_favor.append(i[0])

    # 查询用户评价过的书 的相似书及其相似度
    similar_sql = 'SELECT bookId1,bookId2,similar FROM item_cf_similar WHERE bookId1=%s'
    result_similar_code, similar_result = dbOptions.cf_query_similar(similar_sql, favor_sql_result_topK)

    # similar_result 排序，取前N=30个
    similar_result.sort(key=lambda x: x['similar'], reverse=True)
    similar_list = similar_result[0:N]

    # TO DO 过滤掉用户喜欢的书  favor_sql_result
    similar_filter = list(filter(lambda x: x['bookId'] not in user_favor, similar_list))


    # 去重


    # 查找完整的书本信息
    msg_sql = 'SELECT bookId,bookName,author,imgUrl,subjectUrl FROM br_books WHERE bookId=%s'
    msg_reason_sql = 'SELECT bookName FROM br_books WHERE bookId=%s'

    # 查详细 信息
    cf_result_code, cf_result = dbOptions.cf_query_similar_msg(msg_sql, msg_reason_sql, similar_filter)

    return cf_result


def contentRecommend(userId, favor_list):
    """
    基于内容推荐 的即时处理
    :param userId: 
    :return: 
    """
    # 预处理：取前10本 最近最喜爱喜爱 的书籍， 然后随机选3本，并根据书籍特征分别选出 各 最佳500本，来算相似度，减少计算耗时
    # 返回这两本书的相似列表 合并
    return contentRecDeal(favor_list)


def contentRecDeal(favor_list):
    """
    基于内容推荐 处理
    :param favor_list: 
    :return: 
    """
    # 取前10本 最近最喜爱喜爱 的书籍， 然后随机选3本
    if len(favor_list) > 12:
        favor_list_pre3 = random.sample(favor_list[0:12], 3)
    else:
        favor_list_pre3 = random.sample(favor_list, 3)

    # 分别取 此2本书籍的第1个标签，取出相同Tag标签数
    sql = """
    SELECT tag1.bookId, COUNT(tag1.bookId) FROM br_tags AS tag1
    RIGHT JOIN br_tags AS tag2
    ON tag1.tagName = tag2.tagName
    WHERE tag2.bookId=%s
    
    GROUP BY tag1.bookId
    HAVING COUNT(tag1.bookId)<8 AND COUNT(tag1.bookId)>4
    ORDER BY COUNT(tag1.bookId) DESC
    """

    result_code, result = dbOptions.contRec_query(sql, favor_list_pre3)

    if result_code == 0:
        return result
    else:
        return []


# def cosinSimilar(bookId, list):
#     """
#         计算余弦相似度（权重是RatingNum和RatingScore相关的系数），并排序取TOP N
#     """
#     return []


class cfThread(threading.Thread):
    """
    cf 推荐 的多线程类
    """

    def __init__(self, userId, favor_list, threadName):
        threading.Thread.__init__(self)
        self.userId = userId
        self.threadName = threadName
        self.favor_list = favor_list
        self.result = []

    def run(self):
        # print("开始线程：" + self.threadName)
        # 返回cfRecommend的处理结果
        self.result = cfRecommend(self.userId, self.favor_list)
        # print("退出线程：" + self.threadName)

    def get_result(self):
        return self.result


class contentThread(threading.Thread):
    """
    内容推荐 的多线程类
    """

    def __init__(self, userId, favor_list, threadName):
        threading.Thread.__init__(self)
        self.userId = userId
        self.threadName = threadName
        self.favor_list = favor_list
        self.result = []

    def run(self):
        # print("开始线程：" + self.threadName)
        # 返回contentRecommend的处理结果
        self.result = contentRecommend(self.userId, self.favor_list)
        # print("退出线程：" + self.threadName)

    def get_result(self):
        return self.result
