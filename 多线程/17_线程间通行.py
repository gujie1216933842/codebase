from queue import Queue
'''使用queue是线程安全的'''
import time, threading


def get_detail_html(queue):
    # 爬取文章详情

    while True:
        url = queue.get()
        print('get detail html start')
        time.sleep(2)
        print('get detail html end')


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print('get detail url start')
        time.sleep(4)
        for i in range(20):
            queue.put('http://www.baidu.com/{}'.format(i))

        print('get detail url end')


'''线程通信方式,共享变量'''

if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=100)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()

    # detail_url_queue.task_done()
    detail_url_queue.join()

    print("last time: {}".format(time.time() - start_time))
