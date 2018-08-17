
from multiprocessing import Pool
import time

def get_html(sleep_time):
    print('start')
    time.sleep(sleep_time)
    print('end')


if __name__ == '__main__':
    print(111)
    pool = Pool()
    pool.apply_async(get_html,args=(3,))
    pool.apply_async(get_html,args=(4,))
    pool.close()