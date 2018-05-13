from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


@require_http_methods(["POST"])
def handle_logout(request):
    """
    '''退出'''
    :param request: 
    :return: 
    """
    try:
        token = request.POST.get('token')
        print(token)
        del_sql = 'DELETE FROM my_token WHERE token = %s'
        code = dbOptions.token_delete_token(del_sql, token)

        if code == 0:
            data = {
                'nickName': '游客',
                'state': '成功退出',
                'userId': '',
            }
            return JsonResponse(package.successPack(data))
        else:
            return JsonResponse(package.errorPack('token移除异常！'))
    except Exception as e:
        print(e)
        return JsonResponse(package.errorPack('退出异常！'))