import threading

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