from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

'''
线程池,为什么要用线程池
主线程中可以获取某一个线程的状态或者某一个任务的状态,以及返回值
当一个线程完成的时候我们主线程能立即知道
futures可以让多线程和多进程编码接口一致
'''
import time


def get_html(times):
    time.sleep(times)
    print("get times {} success".format(times))
    return times


excutor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中,submit方法是立即返回
task1 = excutor.submit(get_html, (3))
task2 = excutor.submit(get_html, (2))
#done方法,用于判定某个任务是否完成
print(task1.done())
time.sleep(3)
print(task1.done())


#result方法可以获取task的执行结果
print(task1.result())


'''
task2.cancel()  返回bool
如果线程已经开始执行了,不能cancel(),会返回false
可以把线程池中max_workers 设置为1 , task2.cancel()会返回true

'''


