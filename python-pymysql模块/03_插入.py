import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    db='python_spider',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()  # 最终返回数据类型元组
# cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)  #最终返回数据类型字典

# 查询数据
sql = "insert into my_test(name ,price,goods_comment,raw_add_time) VALUES (%s,%s,%s,now())"
# data = (1)
cursor.execute(sql, ('大名','98',4))  # 如果没有参数就不传,大于等于两个需要写成tuple形式

print('行数:%s' % cursor.rowcount)
affect = cursor.rowcount
connect.commit()  ##提交事务,这行代码一定不能忘记,不然update会不成功
cursor.close()
connect.close()

