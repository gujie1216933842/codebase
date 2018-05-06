import pymysql  #导入 pymysql  
#https://blog.csdn.net/qq_37176126/article/details/72824106 
#打开数据库连接  

db= pymysql.connect(host="47.97.165.75",user="root",  
    password="123",db="ihome",port=3306,charset="utf8")  
  
# 使用cursor()方法获取操作游标  
cur = db.cursor()  
  
#1.查询操作  
# 编写sql 查询语句  user 对应我的表名  
sql = "select * from ih_user_profile"  
try:  
    cur.execute(sql)    #执行sql语句  
  
    results = cur.fetchall()    #获取查询的所有记录  
    #print("id","name","password")  
    #遍历结果  
    for row in results :  
        up_name = row[0]  
        up_mobile = row[1]  
        up_real_name = row[2]  
        print(row)
except Exception as e:  
    raise e  
finally:  
    db.close()  #关闭连接  