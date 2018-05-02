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
    pass