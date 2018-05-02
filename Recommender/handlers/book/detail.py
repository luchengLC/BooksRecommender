from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math

from Recommender.handlers.util import dbOptions, package

'''书本详细信息  需要连表查询 标签 、 是否已被该用户评分等'''


@require_http_methods(["GET"])
def handle_book_detail(request):
    userId = request.GET.get("userId")  # userId的可能为空===》 用户未登录  不直接从cookie中获取，避免session错误
    bookId = request.GET.get("bookId")

    sql = 'SELECT bookId, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary FROM br_books WHERE bookId = %s'
    sql_tag = 'SELECT tagName, bookTagRank FROM br_tags WHERE bookId = %s ORDER BY bookTagRank'

    result_code, result = dbOptions.detail_query(sql, sql_tag, bookId)

    # 返回一个loginState字段， 用于判断是否展示用户对该书本的的评分

    if userId == '' or userId is None:
        data = {
            'loginState': 0,
            'loginMsg': '未登录',
            'bookMsg': result
        }
    else:
        sql_favor_star = 'SELECT starNum FROM favor WHERE userId=%s AND bookId=%s'
        result_favor_code, starMsg = dbOptions.star_query(sql_favor_star, userId, bookId)
        data = {
            'loginState': 1,
            'loginMsg': '已登录',
            'bookMsg': result,
            'starMsg': starMsg,
        }

    if result_code == 0:
        return JsonResponse(package.successPack(data))
    elif result_code == 1:
        return JsonResponse(package.successPack(data))
    else:
        return JsonResponse(package.errorPack(data))
