import pymysql


def search(sql, params):
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
        cur.execute(sql, params)   # 执行
        lists = []
        lists = cur.fetchall()
        res = []
        for i in range(len(lists)):
            temp = {}
            temp['bookId'] = lists[i][0]
            temp['bookName'] = lists[i][1]
            temp['subjectUrl'] = lists[i][2]
            temp['imgUrl'] = lists[i][3]
            temp['author'] = lists[i][4]
            temp['pubDate'] = lists[i][5]
            temp['publisher'] = lists[i][6]
            temp['ratingScore'] = lists[i][7]
            temp['ratingNum'] = lists[i][8]
            temp['price'] = lists[i][9]
            temp['ISBN'] = lists[i][10]
            temp['summery'] = lists[i][11]
            res.append(temp)
        return 0, res  # res可能为空，后续处理
    except Exception as e:
        print("SQL searching Erorr ==== ", e)
        return 1, '搜索出现错误，请重试！'
    finally:
        if db != '':
            db.close()  # 关闭连接


def search_count(sql, params):
    try:
        db = ''
        db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="recommender", port=3306,
                             charset="utf8")
        cur = db.cursor()  # 获取操作游标
          # 执行
        res = 0
        cur.execute(sql, params)
        res = cur.fetchone()[0]

        print('search_count =======', res)
        return res  # res是数字
    except Exception as e:
        print("SQL searching_page Erorr ==== ", e)
        return 0   # 出错就返回0页
    finally:
        if db != '':
            db.close()  # 关闭连接