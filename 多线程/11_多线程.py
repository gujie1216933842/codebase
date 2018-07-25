import threading
import time
def run1():
    print('run1 start')
    time.sleep(3)
    print('run1 end')


def run2():
    print("run2 start")
    time.sleep(4)
    print('run2 end')


t1 = threading.Thread(target=run1,)
t2 = threading.Thread(target=run2,)

t1.start()
t2.start()