from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''注册'''
@require_http_methods(["POST"])
def handle_register(request):
    userId = request.POST.get('userId')
    password = request.POST.get('password')
    nickname = request.POST.get('nickname')
    email = request.POST.get('email')
    print(userId, ' ', password , ' ', nickname, ' ', email)
    msg = {
        'userId': userId,
        'password': password,
        'nickname': nickname,
        'email': email
    }
    sql = 'INSERT INTO users(userId, password, nickname, email) VALUES(%s,%s,%s,%s)'

    result_code, result = dbOptions.register_insert(sql, msg)

    if result_code == 0:
        # session 设置
        request.session['nickname'] = nickname
        request.session['userId'] = userId
        # session data: 2 days
        request.session.set_expiry(60 * 60 * 24 * 2)
        data = {
            'nickname': result
        }
        return JsonResponse(package.successPack(data))
    else:
        return JsonResponse(package.errorPack('注册失败，您的手机号码可能已被注册，请重试！'))