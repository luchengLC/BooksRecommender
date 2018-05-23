from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


@require_http_methods(["POST"])
def handle_favor_add(request):
    userId = request.POST.get('userId')
    bookId = request.POST.get('bookId')
    starNum = request.POST.get('starNum')
    starTime = request.POST.get('starTime')

    print('starTime ***')
    print(starTime)

    print(starTime)
    msg = {
        'userId': userId,
        'bookId': bookId,
        'starNum': starNum,
        'starTime': starTime,
    }
    sql = 'INSERT INTO favor(userId, bookId, starNum, starTime) VALUES(%s, %s, %s, %s)'
    result_code = dbOptions.favor_insert(sql, msg)
    if result_code == 0:
        return JsonResponse(package.successPack(msg))
    else:
        return JsonResponse(package.errorPack('评分失败，您可能已评分或者书籍不存在！'))


@require_http_methods(["POST"])
def handle_favor_query(request):
    userId = request.POST.get('userId')

    # 连表查询返回
    sql = 'SELECT userId, favor.bookId, starNum, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary  FROM favor INNER JOIN br_books ON favor.bookId = br_books.bookId WHERE userId=%s ORDER BY starTime DESC'
    result_code, result = dbOptions.favor_query(sql, userId)
    data = {
        'list': result
    }
    if result_code == 0:
        return JsonResponse(package.successPack(data))
    else:
        return JsonResponse(package.errorPack(result))


@require_http_methods(["POST"])
def handle_favor_delete(request):
    userId = request.POST.get('userId')
    bookId = request.POST.get('bookId')
    msg = {
        'userId': userId,
        'bookId': bookId,
        'msg': '成功移除！'
    }
    # DELETE FROM favor WHERE userId = %s AND bookId = %s
    sql = 'DELETE FROM favor WHERE userId = %s AND bookId = %s'
    result_code = dbOptions.favor_delete(sql, msg)
    if result_code == 0:
        return JsonResponse(package.successPack(msg))
    else:
        return JsonResponse(package.errorPack('移除失败，请重试！'))


@require_http_methods(["POST"])
def handle_favor_star_query(request):
    userId = request.POST.get('userId')  # userId可能是空值'' , 可以先在前台处理
    bookId = request.POST.get('bookId')
    sql = 'SELECT starNum, starTime FROM favor WHERE userId=%s AND bookId=%s'
    result_code, result = dbOptions.star_query(sql, userId, bookId)
    if result_code == 0:
        return JsonResponse(package.successPack(result))
    else:
        return JsonResponse(package.errorPack(result))
