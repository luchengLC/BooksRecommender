import random

import pymysql


def search(sql, params):
    """
    模糊查询 书籍列表 api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, params)  # 执行
        lists = []
        lists = cur.fetchall()
        res = []
        for i in range(len(lists)):
            temp = {
                'bookId': lists[i][0],
                'bookName': lists[i][1],
                'subjectUrl': lists[i][2],
                'imgUrl': lists[i][3],
                'author': lists[i][4],
                'pubDate': lists[i][5],
                'publisher': lists[i][6],
                'ratingScore': lists[i][7],
                'ratingNum': lists[i][8],
                'price': lists[i][9],
                'ISBN': lists[i][10],
                'summary': lists[i][11],
            }
            res.append(temp)
        db.commit()
        return 0, res  # res可能为空，后续处理
    except Exception as e:
        print("SQL searching Erorr ==== ", e)
        return 1, '搜索出现错误，请重试！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def search_count(sql, params):
    """
    模糊查询 书籍总数 api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        # 执行
        res = 0
        cur.execute(sql, params)
        res = cur.fetchone()[0]
        db.commit()

        print('search_count =======', res)
        return res  # res是数字
    except Exception as e:
        print("SQL searching_page Erorr ==== ", e)
        return 0  # 出错就返回0页
    finally:
        if db != '':
            db.close()  # 关闭连接


def register_insert(sql, params):
    """
    注册 api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, (params['userId'], params['password'], params['nickname'], params['email']))  # 执行
        db.commit()
        return 0, params['nickname']
    except Exception as e:
        print('register  Erorr ===== ', e)
        return 1, '注册出错， 估计是账号已被注册，请换账号！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def login_query(sql, param):
    """
    登录 api
    :param sql: 
    :param param: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, param)  # 执行
        res = cur.fetchall()
        db.commit()
        if len(res) == 1:
            # print(res)
            return 0, res[0]
        elif len(res) == 0:
            return 1, '没有查找到对应用户！请您登陆注册！'
        else:
            return 2, '系统错误，多个用户同账号！'
    except Exception as e:
        print('register  Erorr ===== ', e)
        return 3, '登录操作错误！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def favor_insert(sql, params):
    """
    喜爱列表增加item api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, (params['userId'], params['bookId'], params['starNum'], params['starTime']))  # 执行
        db.commit()
        return 0  # 成功
    except Exception as e:
        print('rate add  Erorr ===== ', e)
        return 1
    finally:
        if db != '':
            db.close()  # 关闭连接


def favor_delete(sql, params):
    """
    喜爱列表 移除item api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, (params['userId'], params['bookId']))  # 执行
        db.commit()
        return 0  # 成功
    except Exception as e:
        print('register  Erorr ===== ', e)
        return 1
    finally:
        if db != '':
            db.close()  # 关闭连接


def favor_query(sql, params):
    """
    喜爱列表 某用户查询 按星数返回 api
    :param sql: 
    :param params: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, params)  # 执行
        lists = cur.fetchall()  # 取得全部

        # 按评价的星级返回
        star_1 = []
        star_2 = []
        star_3 = []
        star_4 = []
        star_5 = []
        res = {
            'star_1': star_1,
            'star_2': star_2,
            'star_3': star_3,
            'star_4': star_4,
            'star_5': star_5,
        }
        for i in range(len(lists)):
            temp = {
                'bookId': lists[i][1],
                'starNum': lists[i][2],
                'bookName': lists[i][3],
                'subjectUrl': lists[i][4],
                'imgUrl': lists[i][5],
                'author': lists[i][6],
                'pubDate': lists[i][7],
                'publisher': lists[i][8],
                'ratingScore': lists[i][9],
                'ratingNum': lists[i][10],
                'price': lists[i][11],
                'ISBN': lists[i][12],
                'summary': lists[i][13],
            }
            if lists[i][2] == 1:
                star_1.append(temp)
            elif lists[i][2] == 2:
                star_2.append(temp)
            elif lists[i][2] == 3:
                star_3.append(temp)
            elif lists[i][2] == 4:
                star_4.append(temp)
            elif lists[i][2] == 5:
                star_5.append(temp)

        db.commit()
        return 0, res  # 成功
    except Exception as e:
        print('favor  Erorr ===== ', e)
        return 1, '查询失败'
    finally:
        if db != '':
            db.close()  # 关闭连接


def favor_list_query(sql, userId):
    """
    favor query list  返回的是列表、元组嵌套
    :param sql: 
    :param userId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, userId)  # 执行
        lists = cur.fetchall()  # 取得全部
        return 0, lists
    except Exception as e:
        print('tags  Erorr ===== ', e)
        return 1, '标签推荐处理过程中，喜爱列表处理失败！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def detail_query(sql, sql_tags, bookId):
    """
    书本详细信息查询 api
    :param sql: 
    :param sql_tags: 
    :param bookId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, bookId)  # 执行
        res_book = cur.fetchall()
        db.commit()

        if len(res_book) == 1:
            cur.execute(sql_tags, bookId)
            res_tag_tmp = cur.fetchall()
            db.commit()
            res_tag = []
            for i in res_tag_tmp:
                tmp = {
                    'tagName': i[0],
                    'tagRank': i[1],
                }
                res_tag.append(tmp)

            res = {
                'bookId': res_book[0][0],
                'bookName': res_book[0][1],
                'subjectUrl': res_book[0][2],
                'imgUrl': res_book[0][3],
                'author': res_book[0][4],
                'pubDate': res_book[0][5],
                'publisher': res_book[0][6],
                'ratingScore': res_book[0][7],
                'ratingNum': res_book[0][8],
                'price': res_book[0][9],
                'ISBN': res_book[0][10],
                'summary': res_book[0][11],
                'tags': res_tag
            }
            return 0, res
        else:
            res = '没有查询到对应图书详细信息！'
            return 1, res
    except Exception as e:
        print('register  Erorr ===== ', e)
        return 2, '查询出错!'
    finally:
        if db != '':
            db.close()  # 关闭连接


def star_query(sql, userId, bookId):
    """
    查询某用户对某书的评分 api
    可能没有评分
    :param sql: 
    :param userId: 
    :param bookId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, (userId, bookId))  # 执行
        res_tmp = cur.fetchall()
        db.commit()
        if len(res_tmp) == 1:  # 没有查询到==该用户没有对此书评价过
            print(res_tmp)
            res = {
                'starState': 1,  # 有评价
                'msg': '已评价',  # 有评价
                'star': res_tmp[0][0],
                'starTime': res_tmp[0][1]
            }
        else:
            res = {
                'starState': 0,  # 没有评价
                'msg': '未评价',  # 没有评价
                'star': 0,
            }
        return 0, res
    except Exception as e:
        print('rate  Erorr ===== ', e)
        res = {
            'starState': 0,  # 没有评价
            'msg': '用户评分查询异常!'
        }
        return 1, res
    finally:
        if db != '':
            db.close()  # 关闭连接



def tag_query(sql, bookId):
    """
    标签查询
    :param sql: 
    :param bookId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, bookId)
        res_tag_tmp = cur.fetchall()
        db.commit()
        res_tag = []
        for i in res_tag_tmp:
            tmp = {
                'tagName': i[0],
                'tagRank': i[1],
            }
            res_tag.append(tmp)
        return 0, res_tag
    except Exception as e:
        print('tag query  Erorr ===== ', e)
        return 1, ''
    finally:
        if db != '':
            db.close()  # 关闭连接



def favor_all_query(sql):
    """
    查询全部喜爱列表
    :param sql: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)
        result = cur.fetchall()
        return 0, result
    except Exception as e:
        print('favor all query  Erorr ===== ', e)
        return 1, ''
    finally:
        if db != '':
            db.close()  # 关闭连接


def cf_rec_query(sql, dic):
    """
    cf 查询该用户的评价，做成dict伪矩阵
    :param sql: 
    :param dic: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        res = []
        for k, v in dic.items():
            print(k)
            print(v)
            cur.execute(sql, k)
            resTmp = cur.fetchall()
            print(resTmp)
            tmp = {
                'bookId': resTmp[0][0],
                'bookName': resTmp[0][1],
                'subjectUrl': resTmp[0][2],
                'imgUrl': resTmp[0][3],
                'author': resTmp[0][4],
                # 'pubDate': resTmp[0][5],
                # 'publisher': resTmp[0][6],
                # 'ratingScore': resTmp[0][7],
                # 'ratingNum': resTmp[0][8],
                # 'price': resTmp[0][9],
                # 'ISBN': resTmp[0][10],
                # 'summary': resTmp[0][11],
                'recCoefficient': v,
            }
            res.append(tmp)
        return 0, res
    except Exception as e:
        print('query rec list msg Erorr ===== ', e)
        return 1, 'item-CF获取推荐列表出错！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def hot_query(sql):
    """
    查询热门书籍
    :param sql: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql)
        res = cur.fetchall()
        ress = []
        for i in res:
            tmp = {
                'bookId': i[0],
                'bookName': i[1],
                'subjectUrl': i[2],
                'imgUrl': i[3],
                'author': i[4],
                # 'ratingNum': int(i[5])
            }
            ress.append(tmp)
        return 0, ress

    except Exception as e:
        print('query hot list Erorr ===== ', e)
        return 1, '获取热门书籍列表异常！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def cf_insert_update(list):
    """
    定时任务 计算得到新的 item-cf相似度时，插入
    :param list: 
    :return: 
    """
    sql = 'INSERT INTO item_cf_similar(bookId1, bookId2, similar) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE bookId1=%s,bookId2=%s,similar=%s'
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        for i in list:
            cur.execute(sql, (i['bookId1'], i['bookId2'], i['similar'], i['bookId1'], i['bookId2'], i['similar']))
            db.commit()
        return 0, 'success'
    except Exception as e:
        print('query hot list Erorr ===== ', e)
        return 1, '插入cf相似度 列表异常！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def cf_query_user_favor(sql, userId):
    """
    查找用户的喜爱列表前几个
    :param sql: 
    :param userId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        res = []
        cur.execute(sql, userId)
        res = cur.fetchall()
        db.commit()
        return 0, res
    except Exception as e:
        print('query hot list Erorr ===== ', e)
        return 1, 'cf 查找用户的喜爱列表前几个！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def cf_query_similar(sql, list):
    """
    cf 查询 item-cf 相似度表
    :param sql: 
    :param list: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        res = []
        ress = []
        for i in list:
            cur.execute(sql, i[0])
            res = cur.fetchall()
            for j in res:
                tmp = {
                    'bookId': j[1],
                    'similar': j[2] * i[1],  # 算法的一部分，乘以评分矩阵
                    'reasonBookId': j[0],
                    'method': 'cf'
                }
                ress.append(tmp)
            db.commit()
        return 0, ress
    except Exception as e:
        print('query hot list Erorr ===== ', e)
        return 1, 'cf 查找相似度！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def cf_query_similar_msg(sql, sql_reason, list):
    """
    cf 查询得到相似度的bookId后继续查找book其余信息
    :param sql: 
    :param sql_reason: 
    :param list: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        for i in list:
            cur.execute(sql, i['bookId'])
            res1 = cur.fetchone()
            i['bookName'] = res1[1]
            i['author'] = res1[2]
            i['imgUrl'] = res1[3]
            i['subjectUrl'] = res1[4]
            cur.execute(sql_reason, i['reasonBookId'])
            res2 = cur.fetchone()
            i['reason'] = '喜欢《' + res2[0] + '》的人也喜欢此书。（BY item-CF）'
            # print(i)
        db.commit()
        return 0, list
    except Exception as e:
        print('Erorr ===== ', e)
        return 1, 'cf 查找书本详细信息异常！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def contRec_query(sql, list):
    """
    基于内容推荐 查询与用户喜欢列表random出的几项有较多相同标签的书籍
    :param sql: 
    :param list: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        result = []
        for i in list:
            cur.execute(sql, i[0])
            res = cur.fetchall()
            ress = []
            cur.execute('SELECT bookName FROM br_books WHERE bookId=%s', i[0])
            book_name = cur.fetchone()[0]
            for j in res:
                cur.execute('SELECT bookId,bookName,author,imgUrl,subjectUrl FROM br_books WHERE bookId=%s', j[0])
                rec_book_msg = cur.fetchone()
                tmp = {
                    'bookId': j[0],
                    'bookName': rec_book_msg[1],
                    'author': rec_book_msg[2],
                    'imgUrl': rec_book_msg[3],
                    'subjectUrl': rec_book_msg[4],
                    'reasonBookId': i[0],
                    'reason': '此书与你喜欢的《' + book_name + "》内容相似。（BY CB）",
                    'sameTagsNum': j[1],
                }
                ress.append(tmp)
            # 只取前4
            if len(ress)<5:
                result += ress
            else:
                result += random.sample(ress, 4)
        db.commit()
        return 0, result
    except Exception as e:
        print('content rec query Erorr ===== ', e)
        return 1, 'content 查找书本异常！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def token_delete(sql, userId):
    """
    token删除、清除
    :param sql: 
    :param userId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, userId)
        # res = cur.fetchall()
        db.commit()
        return 0
    except Exception as e:
        print('token_delete Erorr ===== ', e)
        return 1
    finally:
        if db != '':
            db.close()  # 关闭连接


def token_delete_token(sql, token):
    """
    token删除、清除
    :param sql: 
    :param userId: 
    :return: 
    """
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, token)
        # res = cur.fetchall()
        db.commit()
        return 0
    except Exception as e:
        print('token_delete Erorr ===== ', e)
        return 1
    finally:
        if db != '':
            db.close()  # 关闭连接


def token_add(sql, token, userId, endTime):
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, (token, userId, endTime))
        # res = cur.fetchall()
        db.commit()
        return 0
    except Exception as e:
        print('token_add Erorr ===== ', e)
        return 1
    finally:
        if db != '':
            db.close()  # 关闭连接


def token_query(sql, token):
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, token)
        res = cur.fetchall()
        db.commit()
        # token,my_token.userId,endTime,nickname
        if len(res) == 1:
            tmp = {
                'userId': res[0][1],
                'endTime': int(res[0][2]),
                'nickName': res[0][3],
            }
            return 0, tmp
        else:
            return 1, ''
    except Exception as e:
        print('token query error ===== ', e)
        return 1, ''
    finally:
        if db != '':
            db.close()  # 关闭连接