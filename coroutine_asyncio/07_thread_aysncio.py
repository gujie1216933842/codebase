import asyncio
from concurrent.futures import ThreadPoolExecutor

'''
asyncio异步编程方案
协程里面是不能加入某些阻塞io的
但是某些库或者某一个接口,只能提供阻塞io,我们怎么办?
解决方案:我们把它放到一个线程中去做,
即在协程中集成阻塞io,比如我们的pymysql库就是阻塞的

'''

'''在asyncio中集成线程池'''

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))  # 阻塞不会消耗cpu

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    print(data)
    html_data = data.split("\r\n\r\n")[1]
    client.close()


if __name__ == "__main__":
    import time

    start_time = time.time()
    loop = asyncio.get_event_loop()
    excutor = ThreadPoolExecutor()
    tasks = []
    for i in range(20):
        url = "http://www.baidu.com/"
        print(url)
        task = loop.run_in_executor(excutor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:{}".format(time.time() - start_time))
