from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework import permissions
from Recommender.handlers.user.login import create_token

'''注册'''
@require_http_methods(["POST"])
def handle_register(request):
    userId = request.POST.get('userId')
    password = request.POST.get('password')
    nickname = request.POST.get('nickname')
    email = request.POST.get('email')
    startTime = int(request.POST.get('startTime'))  # 前端传来的时间戳:10位int
    msg = {
        'userId': userId,
        'password': password,
        'nickname': nickname,
        'email': email
    }

    # TO DO
    # insert 之前 先查询一下有没有该账号
    sql = 'INSERT INTO users(userId, password, nickname, email) VALUES(%s,%s,%s,%s)'

    result_code, result = dbOptions.register_insert(sql, msg)

    if result_code == 0:
        # 生成token并存好
        token_code, token, endTime = create_token(userId, startTime)
        if token_code == 0:
            data = {
                'nickName': result,
                'token': token,
                'endTime': endTime,
                'userId': userId
            }
            return JsonResponse(package.successPack(data))
        else:
            return JsonResponse(package.errorPack('生成token失败！请重试！'))
    else:
        return JsonResponse(package.errorPack('注册失败，您的手机号码可能已被注册，请重试！'))