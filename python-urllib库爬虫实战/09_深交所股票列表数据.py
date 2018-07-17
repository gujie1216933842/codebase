import urllib.request
import json, re, random
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
    sql = "insert into sz_stock_list(company_code ,A_code,A_short_name,stock_date,general_capital,flow_capital,trade ,name, detail_url,raw_add_time) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    param = tuple(item.values())
    print(param)
    cursor.execute(sql, param)  # 如果没有参数就不传,大于等于两个需要写成tuple形式
    affect = cursor.rowcount
    connect.commit()  ##提交事务,这行代码一定不能忘记,不然update会不成功
    cursor.close()
    connect.close()


if __name__ == "__main__":
    for i in range(1, 107):
        url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO=%s&random=%s" % (
            i, random.random())
        data = urllib.request.urlopen(url).read()
        dict_data = json.loads(data)
        for item in dict_data[0]['data']:
            print(item)
            item['name'] = re.compile("<u>(.*?)</u></a>").findall(item['gsjc'])[0]
            item['detail_url'] = re.compile("href='(.*?)'").findall(item['gsjc'])[0]
            item.pop('gsjc')
            insert_mysql(item)
