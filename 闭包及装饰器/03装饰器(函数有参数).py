# Author:Bob
'''装饰器装饰有参数的函数'''

def func(fun_name):
    def func_inner(*args, **kwargs):
        print("hahaha")
        fun_name(*args, **kwargs)

    return func_inner

@func
def index(a):
    print("展示首页")

index(1)

