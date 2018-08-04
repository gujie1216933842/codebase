
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
    progress1.join()
    progress2.join()
    print('main progress end')
    '''加了join函数可以,统计整理多进程处理需要的时间,这里可对比多线程,比较两者之间消耗的时间'''
    print('comsume:{}:'.format(time.time() - start_time))
