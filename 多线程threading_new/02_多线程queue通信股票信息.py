from queue import Queue

'''
爬取深交所高管买卖
把链接地址存放在队列queue中

使用queue是线程安全的
如果使用全局变量进行线程间的通信,会有线程安全问题
'''
import time, threading, random, requests


def put_url(queue):
    '''把连接放入队列'''
    for i in range(50):
        queue.put(
            "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
                i, random.random()))


def get_stock_data(queue):
    '''从队列中取链接'''
    while True:
        url = queue.get()
        res = requests.get(url)
        if res.status_code == 200:
            print(res.text)
        # return data


if __name__ == '__main__':
    url_queue = Queue(maxsize=100)
    put_thread = threading.Thread(target=put_url, args=(url_queue,))
    put_thread.start()
    '''开启10个线程'''
    for i in range(5):
        print(i)
        get_thread = threading.Thread(target=get_stock_data, args=(url_queue,))
        get_thread.start()
