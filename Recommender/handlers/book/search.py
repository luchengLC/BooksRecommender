from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math

from Recommender.handlers.util import dbOptions, package


@require_http_methods(["GET"])
def handle_search(request):
    wd = parse.unquote(request.GET.get('wd'))  # url解码
    # print('wd = ', wd)
    pageno = int(request.GET.get('pageno'))  # 转换成整型
    # order = request.GET.get('order')

    search_sql_base = 'FROM br_books WHERE MATCH(bookName, author) AGAINST(%s IN NATURAL LANGUAGE MODE)'

    # 求对应列表
    count = (pageno - 1) * 20  # 用于辅助翻页
    sql = 'SELECT bookId, bookName, subjectUrl, imgUrl, author, pubDate, publisher, ratingScore, ratingNum, price, ISBN, summary '+ search_sql_base + ' LIMIT '+str(count)+',20;'
    lists = []  # 返回的参数列表
    result_code, lists = dbOptions.search(sql, wd)

    # 求页数page_count
    sql_count = 'SELECT COUNT(bookId) ' + search_sql_base
    counts = int(dbOptions.search_count(sql_count, wd))  # 查询到对应的总数
    page_count = math.ceil(counts/20)  # python3:/是精确除，然后向上取整。每页20

    if result_code == 0:
        data = {
            'page_count': page_count,
            'list': lists
        }
        return JsonResponse(package.successPack(data))
    else:
        return JsonResponse(package.errorPack(lists[0]))