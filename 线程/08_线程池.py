from concurrent.futures import ThreadPoolExecutor
import time


def my_feature(message):
    time.sleep(2)
    return message


pool = ThreadPoolExecutor(max_workers=2)  # 创建一个最大容纳2个task的线程池

f1 = pool.submit(my_feature,'hello')  #使用submit方法来往线程池中加入一个task,返回一个featrue对象,可以理解为一个未完成的操作
f2 = pool.submit(my_feature,'nihao')
print(f1.done())
time.sleep(3)
print(f2.done())

print(f1.result())
print(f2.result())

'''
我们根据运行结果来分析一下。我们使用submit方法来往线程池中加入一个task，submit返回一个Future对象，
对于Future对象可以简单地理解为一个在未来完成的操作。在第一个print语句中很明显因为time.sleep(2)的原因我们的future1没有完成，
因为我们使用time.sleep(3)暂停了主线程，所以到第二个print语句的时候我们线程池里的任务都已经全部结束

linux中:
ziwenxie :: ~ » python example1.py
False
True
hello
world
# 在上述程序执行的过程中，通过ps命令我们可以看到三个线程同时在后台运行
ziwenxie :: ~ » ps -eLf | grep python
ziwenxie      8361  7557  8361  3    3 19:45 pts/0    00:00:00 python example1.py
ziwenxie      8361  7557  8362  0    3 19:45 pts/0    00:00:00 python example1.py
ziwenxie      8361  7557  8363  0    3 19:45 pts/0    00:00:00 python example1.py


'''

