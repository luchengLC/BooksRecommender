from urllib import parse
import copy

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package
import hashlib
from hashlib import sha1


@require_http_methods(["POST"])
def handle_login(request):
    """
    登录
    :param request: 
    :return: 
    """
    userId = request.POST.get('userId')
    pw_in = request.POST.get('password')  # 前端传来的密码：密文
    startTime = request.POST.get('startTime')  # 前端传来的时间戳:10位int
    sql = 'SELECT userId,password,nickname,email FROM users WHERE userId = %s'
    result_code, result = dbOptions.login_query(sql, userId)

    if result_code == 0:
        pw_get = result[1]  # 数据库得到的密码：明文
        check_code = check_pw(pw_in, pw_get)
        if check_code == 0:
            # session 设置
            print(result[2])
            print(result[0])

            # 生成token并存好
            token_code, token, endTime = create_token(userId, int(startTime))

            if token_code == 0:
                data = {
                    'nickname': result[2],
                    'token': token,
                    'endTime': endTime,
                }
                return JsonResponse(package.successPack(data))
            else:
                return JsonResponse(package.errorPack('生成token失败！请重试！'))
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


def create_token(userId, startTime):
    """
    生成token方案：先判断有没有，有的就删，then↓
    没有的就把 userId+endTime做一个摘要，然后+':'+endTime， 然后base64编码
    :param userId: 
    :param startTime: 
    :return: 
    """
    # 先检查一下 token是否存在， 是的话就全删掉
    del_sql = 'DELETE FROM my_token WHERE userId = %s'
    delete_code = dbOptions.token_delete(del_sql, userId)
    endTime = 0

    if delete_code == 0:
        # 不存在就create
        endTime = startTime + 86400
        str1 = userId + str(endTime)
        psw = sha1()
        psw.update(str1.encode('utf8'))
        token = psw.hexdigest() + str(endTime)

        # 存进数据库
        add_sql = 'INSERT INTO my_token(token, userId, endTime) VALUES(%s,%s,%s)'
        add_code = dbOptions.token_add(add_sql, token, userId, endTime)

        if add_code == 0:
            return 0, token, endTime
        else:
            return 1, '', 0
    else:
        return 1, '', 0
