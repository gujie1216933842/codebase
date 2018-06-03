# coding=utf-8

import os

import time

# 判断是否存在脚本的兄弟层级中是否存在log文件
log_path = os.path.join(os.path.dirname(__file__), 'log/')

if not os.path.exists(log_path):
    os.makedirs(log_path)

print(log_path)

# 当前时间


now_day = time.strftime('%Y-%m-%d', time.localtime())
print(now_day)
