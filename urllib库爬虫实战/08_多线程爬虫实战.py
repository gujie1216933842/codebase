'''
多线程爬虫:在我们的程序中某些程序段并行的去执行
'''

import threading
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("我是线程A")

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("我是线程B")

a = A()
a.start()

b = B()
b.start()
