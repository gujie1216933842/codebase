from threading import Thread,Lock
import time
'''
互斥锁加在了for循环外面,实际上形成了串型结构

'''
g_num = 0

def work1():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("在work1()函数中全局变量是: %s" % g_num)


def work2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print('在work2()函数中全局变量是: %s' % g_num)


print('线程创建之前,全局变量: %s' % g_num)

#创建一把互斥锁
mutex = Lock()

t1 = Thread(target=work1)
t1.start()
# time.sleep(1)

t2 = Thread(target=work2)
t2.start()



