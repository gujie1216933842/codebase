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
    t1.start()
    t2.start()
    print('consume:{}s'.format(now() - start_time))
