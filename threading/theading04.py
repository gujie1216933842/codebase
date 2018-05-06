import threading
import time

'''
生成一个红绿灯线程程序
一个线程受另一个线程的影响

'''



def run(n):
    print("task:", n)
    time.sleep(5)


start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' % (i),))
    t.start()
print('cost:', time.time() - start_time)
