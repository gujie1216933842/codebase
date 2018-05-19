# Author:Bob
'''
装饰器装饰有参数的函数
exit(0)：无错误退出
exit(1)：有错误退出



'''


def func(fun_name):
    def func_inner(*args, **kwargs):
        a = args
        print(a)
        if not  a[0]:
            print("请先登录")
            exit()
        else:
            print("已登录,继续往下执行")

        fun_name(*args, **kwargs)

    return func_inner


@func
def index(a):
    print("展示首页")


index(1)
print("-----------------")
index(0)
