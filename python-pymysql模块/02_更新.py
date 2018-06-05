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
sql = "update my_test set name  = %s "
# data = (1)
cursor.execute(sql, ('乔布斯'))  # 如果没有参数就不传,大于等于两个需要写成tuple形式

print('行数:%s' % cursor.rowcount)
affect = cursor.rowcount

cursor.close()
connect.close()

