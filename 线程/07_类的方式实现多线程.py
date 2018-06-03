import threading


class MyThread(threading.Thread):
    def __init__(self,n):
        threading.Thread.__init__(self,n)  
        #super(MyThread, self).__init__()  #这段代码和上面一行用一个作用,应为把把父类中的init方法重构了,必须要重新init()一下
        self.n = n  

    '''
    这里线程要调用的run函数
    注意:这里方法名必须要写成run()
    '''
    def run(self):
         print('线程名:%s')



t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()
