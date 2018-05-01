from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''用于 保持登录状态'''
@require_http_methods(["GET"])
def handle_home(request):
    try:
        if request.session.get('nickname', None):
            nickname = request.session['nickname']
            userId = request.session['userId']
            data = {
                'nickname': nickname,
                'userId': userId,
                'state': '已登录状态'
            }
            return JsonResponse(package.successPack(data))
        else:
            request.session.flush()
            data = {
                'nickname': '游客',
                'userId': '',
                'state': '未登录状态'
            }
            return JsonResponse(package.successPack(data))
    except Exception as e:
        return  JsonResponse(package.errorPack('登录状态维持异常！'))
