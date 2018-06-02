from threading import Thread
import time

g_num = 0


def work1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("在work1()函数中全局变量是: %s" % g_num)


def work2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('在work2()函数中全局变量是: %s' % g_num)


print('线程创建之前,全局变量: %s' % g_num)

t1 = Thread(target=work1)
t1.start()
# time.sleep(1)

t2 = Thread(target=work2)
t2.start()



