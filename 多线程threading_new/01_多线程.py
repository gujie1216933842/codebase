import threading, time


def get_html(sleep_times):
    print('get_html begin.........')
    time.sleep(sleep_times)
    print('get_html end.........')


if __name__ == '__main__':
    print('main thread start')
    now = lambda: time.time()
    start_time = now()
    t1 = threading.Thread(target=get_html, args=(2,))
    t2 = threading.Thread(target=get_html, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('comsume:{}'.format(now() - start_time))
