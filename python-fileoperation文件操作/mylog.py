# coding=utf-8
'''
自己写的日志log模块
'''


import os
import time


def mylog(content):
    # 判断是否存在脚本的兄弟层级中是否存在log文件
    log_path = os.path.join(os.path.dirname(__file__), 'log/')
    try:
        if not os.path.exists(log_path):
            os.makedirs(log_path)  # 创建文件夹
    except Exception as e:
        print('创建文件异常:%s' % e)

    # 判断当天日志文件是否存在

    now_day = time.strftime('%Y-%m-%d', time.localtime())
    log_file_path = os.path.join(os.path.dirname(__file__), 'log/' + str(now_day) + '.log')

    log_file_handle = open(log_file_path, 'a')

    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log_content = "[%s] %s" % (now_time, content)

    log_file_handle.write(log_content)
    log_file_handle.write('\n')

    log_file_handle.close()


if __name__ == "__main__":
    mylog('nihao...........')
