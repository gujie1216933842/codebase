import urllib.request
import json, re, random, datetime
import pymysql.cursors


def insert_mysql(item):
    # 连接数据库
    connect = pymysql.Connect(
        host='47.97.165.75',
        port=3306,
        user='root',
        passwd='123',
        db='stock',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()  # 最终返回数据类型元组

    # 查询数据
    sql = "insert into sz_senior_stock_change_list(stock_code ,stock_name,senior_name,change_date,change_amount,price" \
          ",reason ,change_rate, day_stock_amount,change_name,duty,relationship,raw_add_time) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    param = tuple(item.values())
    print(param)
    cursor.execute(sql, param)  # 如果没有参数就不传,大于等于两个需要写成tuple形式
    affect = cursor.rowcount
    connect.commit()  ##提交事务,这行代码一定不能忘记,不然update会不成功
    cursor.close()
    connect.close()


def select_mysql(sql):
    # 连接数据库
    connect = pymysql.Connect(
        host='47.97.165.75',
        port=3306,
        user='root',
        passwd='123',
        db='stock',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()  # 最终返回数据类型元组
    cursor.execute(sql)  # 如果没有参数就不传,大于等于两个需要写成tuple形式
    ret = cursor.fetchall()
    cursor.close()
    connect.close()
    return ret


if __name__ == "__main__":

    sql = "select change_date from sz_senior_stock_change_list  group  by change_date order by change_date desc"
    ret = select_mysql(sql)
    now = datetime.date.today().strftime("%Y-%m-%d")

    # 数据库中最新的日期
    last_date = ret[0][0].strftime("%Y-%m-%d")
    # 数据库中最新日期前一天
    new_last_date = (ret[0][0] + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
    print(new_last_date)

    url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=1&txtStart=%s&txtEnd=%s&random=%s" % (
        new_last_date, now, random.random())

    data = urllib.request.urlopen(url).read()
    print(type(data))
    dict_data = json.loads(data.decode())

    # 页数
    pages = dict_data[0]['metadata']['pagecount']
    print(pages)

    for i in range(1, pages + 1, 1):
        url1 = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&txtStart=%s&txtEnd=%s&random=%s" % (
            i, new_last_date, now, random.random())
        print(url1)

        data = urllib.request.urlopen(url1).read()
        dict_data_new = json.loads(data.decode())

        for item in dict_data_new[0]['data']:
            print(item)
            # insert_mysql(item)
