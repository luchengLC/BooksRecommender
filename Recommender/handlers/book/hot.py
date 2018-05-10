from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


#  啊啊啊啊啊，用什么 算法
@require_http_methods(["GET"])
def handle_hot_query(request):
    sql = 'SELECT favor.bookId, bookName, subjectUrl, imgUrl, author FROM favor LEFT JOIN br_books ON favor.bookId = br_books.bookId ORDER BY starTime , ratingNum, ratingScore LIMIT 15'
    result_code, result = dbOptions.hot_query(sql)
    if result_code == 0:
        list = {
            'list': result
        }
        return JsonResponse(package.successPack(list))
    else:
        return JsonResponse(package.errorPack(result))

