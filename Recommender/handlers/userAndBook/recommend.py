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
