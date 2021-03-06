from urllib import request
import gevent, time
from gevent import monkey
'''
gevent是python的一个第三方库,可以轻松的通过gevent实现并发同步或者异步编程
在gevent中,主要用到的模式是greenlet,它是以C语言扩展模块接入python的轻量级协程.
greenlet全部运行在主程序操作系统进程的内部,但是他们被协作式的调度


gevent是协程自动切换

'''


'''
如何让gevent知道urllib正在进行io操作
'''
monkey.patch_all()  # 把当前程序所有有可能进行的io操作的地方,在前面打上一个标记
                    # 如果没有这段代码,gevent不能识别urllib进行io操作,程序仍然是串型


def fun1(url):
    print("GET:%s" % url)
    res = request.urlopen(url)
    data = res.read()
    print("%s  bytes received from %s " % (len(data), url))


urls = [
    "http://www.1768.com",
    "http://47.97.165.75",
    "http://www.baidu.com",
]

'''
同步
'''
time_start = time.time()
for url in urls:
    fun1(url)

print("同步 cost: %s" % (time.time() - time_start))

'''
异步
'''
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(fun1, "http://www.1768.com"),
    gevent.spawn(fun1, "http://47.97.165.75"),
    gevent.spawn(fun1, "http://www.baidu.com"),
])

print("异步 cost:%s" % (time.time() - async_time_start))
