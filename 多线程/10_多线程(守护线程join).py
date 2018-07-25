from threading import Thread, current_thread
import time, random


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        sleep_time = random.randint(1, 10)  # 左右的是闭区间
        time.sleep(sleep_time)
        print('线程睡了:%s秒,多线程%s' % (sleep_time, self.getName()))


t1 = MyThread('hh')
t2 = MyThread('jj')
# t1.setDaemon(False)
# t2.setDaemon(True)  #把子线程设置为守护线程,默认不是:false
t1.start()
t1.join()      #主线程运行到这里暂停,等t1子线程启动到结束,主线程才继续往下运行,
t2.start()
t2.join()      #主线程运行到这里暂停,等t2子线程启动到结束,主线程才继续往下运行
print('程序结束')

'''
这里子线程被设置为守护线程,所以当主线程执行结束之后,子线程不管此时执行到哪里,直接跟着挂了
注意:当有多个子线程的时候,有的子线程设为了守护线程,而有的没有,那么只会设为守护线程的哪些线程
     会随着主线程结束而结束,那些非守护线程的哪些子线程被主线程等待

'''








'''
知识点一：
当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行流的最小单元，当设置多线程时，
主线程会创建多个子线程，在python中，默认情况下（其实就是setDaemon(False)），主线程执行完自己的任务以后，
就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束

知识点二：
当我们使用setDaemon(True)方法，设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，
可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止

知识点三：
此时join的作用就凸显出来了，join所完成的工作就是线程同步，即主线程任务结束之后，
进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止

知识点四：
join有一个timeout参数：

当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序。
所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和。简单的来说，就是给每个子线程一个timeout的时间，
让他去执行，时间一到，不管任务有没有完成，直接杀死。
没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，主线程结束，
但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出。

'''
