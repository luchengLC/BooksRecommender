

def successPack(data):
    res = {}
    res['error_code'] = 0
    res['msg'] = 'success'
    res['data'] = data
    return res


def errorPack(err):
    res = {}
    res['error_code'] = 1
    res['msg'] = err
    return res

