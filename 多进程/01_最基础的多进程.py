
'''
多进程编程,最基础
一个主进程开启两个子进程
'''

import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print('sub_progress success')
    return n


if __name__ == "__main__":
    print('main progress start')
    start_time = time.time()
    progress1 = multiprocessing.Process(target=get_html, args=(2,))
    progress2 = multiprocessing.Process(target=get_html, args=(2,))
    progress1.start()
    progress2.start()
    print('main progress end')
    '''这里没有join函数'''
    print('comsume:{}:'.format(time.time() - start_time))
