import time

# 把时间戳转换成格式化字符串

str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('当前格式化时间:%s' % str_time)

# 把格式化之后的时间转化成时间戳
# str_time = "2018-06-05 22:21:19"
time_stamp = time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S"))
print('当前时间戳:%s' % time_stamp)
