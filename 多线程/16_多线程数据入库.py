from concurrent.futures import as_completed, ThreadPoolExecutor
import time, random, requests, json
import pymysql


def insert_mysql(item):
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
    sql = "insert into sz_senior_stock_change_list_bak(stock_code ,stock_name,senior_name,change_date,change_amount,price" \
          ",reason ,change_rate, day_stock_amount,change_name,duty,relationship,raw_add_time) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    param = (
        item['zqdm'], item['zqjc'], item['gdxm'], item['jyrq'], item['bdgs'], item['bdjj'], item['bdyy'],
        item['cgbdbl'], item['cgzs'], item['gdxm'], item['zw'], item['gxlb'])
    print(sql)
    print(param)
    cursor.execute(sql, param)  # 如果没有参数就不传,大于等于两个需要写成tuple形式
    affect = cursor.rowcount
    print(affect)
    connect.commit()  # 提交事务,这行代码一定不能忘记,不然update会不成功
    cursor.close()
    connect.close()
    return affect


def get_data(url):
    res = requests.get(url)
    if res.status_code == 200:
        dict_data = json.loads(res.text)
        list_data = dict_data[0]['data']
        res = insert_mysql(list_data)
        return res

if __name__ == "__main__":
    start_time = time.time()
    excutor = ThreadPoolExecutor(max_workers=1)
    all_tasks = [excutor.submit(get_data, (
            "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
        i, random.random()))) for i in range(1, 2)]

    '''as_complete是一个生成器'''
    for future in as_completed(all_tasks):
        data = future.result()

    print('comsumer:{}'.format(time.time() - start_time))
