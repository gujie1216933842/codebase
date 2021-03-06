
'''
time模块学习
time.time() 生成当前的时间戳，格式为10位整数的浮点数。
time.strftime()根据时间元组生成时间格式化字符串。
time.strptime()根据时间格式化字符串生成时间元组。time.strptime()与time.strftime()为互操作。
time.localtime()根据时间戳生成当前时区的时间元组。
time.mktime()根据时间元组生成时间戳。


区分 strftime()和strptime()的方法,方便记忆
strftime-  str_format_time    格式化(format)
strptime-  str_parse_time     解析(parse)




'''
import time
a = time.time()
b = time.localtime()
print(b)
print(int(a))  #当前时间戳取整
print(b[0])
# time.sleep(2)
print(b.tm_year)

#struct_time转换成 '2018-04-25 14:59:47'格式
d = time.strftime('%Y-%m-%d %H:%M:%S',b)
print(d)

#时间戳转换成'2018-04-25 14:59:47'格式
e = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(a))


#'2018-04-25 14:59:47'格式转化为struct_time
print("***********格式化时间转化成时间戳*************")
f = "2018-04-25 15:10:56"
g = time.strptime(f,'%Y-%m-%d %H:%M:%S')
# struct_time转换成时间戳
h = time.mktime(g)
print(int(h))












