from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''退出'''


# @require_http_methods(["GET"])
def handle_logout(request):
    try:
        if request.session.get('nickname', None):
            request.session.flush()
            data = {
                'nickname': '游客',
                'state': '成功退出'
            }
            return JsonResponse(package.successPack(data))
        else:
            request.session.flush()
            data = {
                'nickname': '游客',
                'state': '未登录'
            }
            return JsonResponse(package.successPack(data))
    except Exception as e:
        return  JsonResponse(package.errorPack('退出异常！'))