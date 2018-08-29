from multiprocessing import Pool
import time


def get_html(sleep_time):
    print('start')
    time.sleep(sleep_time)
    print('end')


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_html, [i for i in range(5)])
