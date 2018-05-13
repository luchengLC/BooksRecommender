from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


@require_http_methods(["GET"])
def handle_hot_query(request):
    """
    热门书籍推荐
    获取最近ratingNum较高的书籍
    :param request: 
    :return: 
    """
    # 还可以优化： 因素：favor此书的人数
    sql = 'SELECT br_books.bookId, bookName, subjectUrl, imgUrl, author,ratingNum,starTime FROM favor LEFT JOIN br_books ON favor.bookId = br_books.bookId  GROUP BY br_books.bookId ORDER BY ratingNum DESC,starTime DESC LIMIT 15'
    result_code, result = dbOptions.hot_query(sql)
    if result_code == 0:
        list = {
            'list': result
        }
        return JsonResponse(package.successPack(list))
    else:
        return JsonResponse(package.errorPack(result))

