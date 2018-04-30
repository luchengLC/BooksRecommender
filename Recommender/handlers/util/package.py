
'''包装返回结构的俩方法'''


def successPack(data):
    res = {
        'error_code': 0,
        'msg': 'success',
        'data': data
    }
    return res


def errorPack(err):
    res = {
        'error_code': 1,
        'msg': err
    }
    return res

