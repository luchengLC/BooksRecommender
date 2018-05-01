from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package
import hashlib

'''登录'''
@require_http_methods(["POST"])
def handle_login(request):
    userId = request.POST.get('userId')
    pw_in = request.POST.get('password')  # 前端传来的密码：密文
    sql = 'SELECT userId,password,nickname,email FROM users WHERE userId = %s'
    result_code, result = dbOptions.login_query(sql, userId)

    if result_code == 0:
        pw_get = result[1]   # 数据库得到的密码：明文
        check_code = check_pw(pw_in, pw_get)
        if check_code == 0:
            # session 设置
            request.session['nickname'] = result[2]
            request.session['userId'] = result[0]
            # session data: 2 days
            request.session.set_expiry(60 * 60 * 24 * 2)
            data = {
                'nickname': result[2]
            }
            return JsonResponse(package.successPack(data))
        else:
            check_msg = '账号密码不匹配！'
            return JsonResponse(package.errorPack(check_msg))
    else:
        return JsonResponse(package.errorPack(result))


def check_pw(pw_in, pw_get):
    # md5加密pw_get
    hl = hashlib.md5()
    hl.update(pw_get.encode(encoding='utf-8'))
    pw_get_md5 = hl.hexdigest()
    if pw_in == pw_get_md5:
        return 0  # 相等，匹配成功
    else:
        return 1  # 不相等，匹配不成功

