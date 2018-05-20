import threading
import time

'''
以for循环启动线程
主线程不会等待子线程的执行

程序在退出之前,一定会确认所有的线程都执行完毕,即相当于一个join
循环50个线程,其实有51个线程 1个主线程和50个子线程
当前程序是主线程

python解释器直接调用c语言的线程接口


'''


def run(n):
    print("task:", n)
    time.sleep(5)


start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' % (i),))
    t.start()
print('cost:', time.time() - start_time)
