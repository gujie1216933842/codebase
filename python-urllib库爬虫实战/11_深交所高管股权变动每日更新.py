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


if __name__ == "__main__":
    # 当前日期
    now = datetime.date.today().strftime("%Y-%m-%d")
    # 两天前
    before = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")

    url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=1&txtStart=%s&txtEnd=%s&random=%s" % (
        before, now, random.random())

    data = urllib.request.urlopen(url).read()
    dict_data = json.loads(data)

    # 页数
    pages = dict_data[0]['metadata']['pagecount']

    for i in range(1, pages + 1, 1):
        url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&txtStart=%s&txtEnd=%s&random=%s" % (
            i, before, now, random.random())

        data = urllib.request.urlopen(url).read()
        dict_data_new = json.loads(data)
        print(dict_data_new[0]['data'])
        for item in dict_data[0]['data']:
            insert_mysql(item)
