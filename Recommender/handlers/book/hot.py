from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''修改 个人信息'''
@require_http_methods(["POST"])
def handle_info_change(request):
    pass


'''查询 个人信息'''
@require_http_methods(["GET"])
def handle_info_query(request):
    pass
