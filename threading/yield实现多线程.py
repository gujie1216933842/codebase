'''yield关键字
如果一个函数中出现yield,这个函数就是生成器
模拟ioloop+epoll实现多线程

yield可以把程序出现堵塞之前和程序程序出现堵塞之后放到一起去
'''

import threading, time

gen = None


def long_io():
    def fun():
        global gen
        print("开始进行耗时操作")
        time.sleep(5)
        print("完成执行耗时操作")
        result = "io result"
        try:
            gen.send(result)  # 作用:把gen生成器拿过来,把ret等于result,然后继续执行下面的代码
        except StopIteration:
            pass

    threading._start_new_thread(fun, ())


def req_a():
    print("开始处理请求a")
    ret = yield long_io()
    print(ret)
    print("离开处理请求a")


def req_b():
    print("开始处理请求b")
    time.sleep(2)
    print("完成处理请求b")


def main():
    global gen
    gen = req_a()
    gen.__next__()
    req_b()
    while 1:
        pass


if __name__ == "__main__":
    main()

    '''
     函数中存在yield关键字,所以函数req_a现在就是一个生成器
     执行函数,调用生成器的next方法,让他往下去执行,
     执行到遇见第一个关键字的时候停止,执行到新的函数  long_io() ,我们发现里面有 函数fun() 和 开启新的线程的操作
    fun()函数我们先忽略,它是作为开启线程的参数被调用的,我们理解为:当执行long_io()操作时,开启新的线程,新线程
    执行的操作就是fun()函数的内容
    开启线程之后,主线程开启子线程的任务已经完成,接下来,主线程继续往下执行,即执行  req_b() ,子线程执行fun()函数,
    互不干扰
    
    理解 gen.send(result) : 
         gen是一个全局的生成器对象,代表整个带有yield关键字的req_a()函数, send()方法,就是把参数result 放到生成器的断点处
          把result 返回给ret , req_a()函数函数接下去执行(起到了一个回调的机制或者说是作用),整个生成器原先已经暂停,我们代码中
          把它拿到新的线程上来重新激活 
     并且把暂停时的状态保存下来
    并且yield返回
    
    
    
    
    '''
