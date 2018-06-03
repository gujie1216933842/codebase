# coding=utf-8

import os

import time

# 判断是否存在脚本的兄弟层级中是否存在log文件
log_path = os.path.join(os.path.dirname(__file__), 'log/')
try:
    if not os.path.exists(log_path):
        os.makedirs(log_path)  #创建文件夹
except Exception as e:
    print('创建文件异常:%s' % e)

# 判断当天日志文件是否存在

now_day = time.strftime('%Y-%m-%d', time.localtime())
log_file_path = os.path.join(os.path.dirname(__file__), 'log/' + str(now_day) + '.log')
print(log_file_path)

log_file_handle = open(log_file_path,'w')

log_file_handle.write('你好!')

log_file_handle.close()




