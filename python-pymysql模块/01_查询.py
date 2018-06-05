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
sql = "SELECT * from my_test WHERE id = %s limit 1 "
# data = (1)
cursor.execute(sql, 1)  # 如果没有参数就不传,大于等于两个需要写成tuple形式

print('行数:%s' % cursor.rowcount)
#ret1 = cursor.fetchall()
ret2 = cursor.fetchone()
print(ret2)

# for row in ret1:
#     print(row)
# print('共查找出', cursor.rowcount, '条数据')

cursor.close()
connect.close()
