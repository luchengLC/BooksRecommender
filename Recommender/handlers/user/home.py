from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


@require_http_methods(["POST"])
def handle_home(request):
    """
    用于 保持登录状态
    :param request: 
    :return: 
    """
    try:
        # 辨认有token是否存在、没有过期
        # 若无，则找到userId对应的userName,返回
        token = request.POST.get('token')
        startTime = int(request.POST.get('startTime'))

        sql = 'SELECT token,my_token.userId,endTime,nickname FROM my_token INNER JOIN users ON my_token.userId = users.userId WHERE token =%s'
        code, msg = dbOptions.token_query(sql, token)
        print('code = = = ', code)
        if code == 0:
            print('endTime - startTime = ')
            print(msg['endTime'], '-', startTime, '=')
            print(msg['endTime']-startTime)
            ge = msg['endTime'] - startTime - 86400
            print('差距 = ', ge)
            if ge <= 0:
                data = {
                    'userId': msg['userId'],
                    'nickName': msg['nickName'],
                    'msg': '登录状态！',
                    'state_code': 0
                }
                return JsonResponse(package.successPack(data))
            else:
                tmp = {
                    'userId': '',
                    'nickName': '游客',
                    'msg': '身份验证已超时！请重新登录！',
                    'state_code': 1  # 超时
                }
                return JsonResponse(package.successPack(tmp))
        else:
            tmp = {
                'userId': '',
                'nickName': '游客',
                'msg': '您还未登录，请重新登录！',
                'state_code': 1  # 超时
            }
        return JsonResponse(package.successPack(tmp))

    except Exception as e:
        print('errrrrr', e)
        return JsonResponse(package.errorPack('登录状态维持异常！'))
