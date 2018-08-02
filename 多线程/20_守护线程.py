import threading
import time


def run1(sleep_times):
    print('start run1')
    time.sleep(sleep_times)
    print('end run1')


def run2(sleep_times):
    print('start run2')
    time.sleep(sleep_times)
    print('end run2')


if __name__ == '__main__':
    now = lambda: time.time()
    start_time = time.time()

    t1 = threading.Thread(target=run1, args=(1,))
    t2 = threading.Thread(target=run2, args=(2,))
    '''这里面把两个线程同时设置为守护线程,主线程执行完,整个程序就停止了'''
    t1.setDaemon(True)  # 设置守护线程,默认为false
    t2.setDaemon(True)  # 设置守护线程,默认为false
    t1.start()
    t2.start()


    print('consume:{}s'.format(now() - start_time))
    '''主线程等待子线程执行完之后,才结束'''