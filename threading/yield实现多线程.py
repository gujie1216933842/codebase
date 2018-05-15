'''yield关键字
如果一个函数中出现yield,这个函数就是生成器
模拟ioloop+epoll实现多线程

yield可以把程序出现堵塞之前和程序程序出现堵塞之后放到一起去
'''

import threading,time

gen = None

def long_io():
    def fun():
        global gen
        print("开始进行耗时操作")
        time.sleep(5)
        print("完成执行耗时操作")
        result = "io result"
        try:
            gen.send(result)  #作用:把gen生成器拿过来,把ret等于result,然后继续执行下面的代码
        except StopIteration:
            pass
    threading._start_new_thread(fun,())



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
    gen = req_a()   #函数中存在yield关键字,所以函数req_a现在就是一个生成器
    gen.__next__()    #执行函数,第一次遇到yield会暂停
    req_b()
    while 1:
        pass


if __name__ == "__main__":
    main()

