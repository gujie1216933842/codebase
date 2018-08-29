from multiprocessing import Process
import time


def get_html(sleep_time):
    print('start')
    time.sleep(sleep_time)
    print('end')


if __name__ == '__main__':
    p1 = Process(target=get_html, args=(3,))
    p2 = Process(target=get_html, args=(4,))

    p1.start()
    p2.start()
