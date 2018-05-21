import threading
''''
Python由于有全锁局的存在（同一时间只能有一个线程执行），
并不能利用多核优势。所以，如果你的多线程进程是CPU密集型的，那多线程并不能带来效率上的提升
，相反还可能会因为线程的频繁切换，导致效率下降；如果是IO密集型，
多线程进程可以利用IO阻塞等待时的空闲时间执行其他线程，
提升效率。



'''
'''
以类的形式
'''


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("run task", self.n)

if __name__ == "__main__":
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()