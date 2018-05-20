''''
装饰器中含有参数
'''


def fun(name):
    def fun_inner(fun_name):
        def fun_inner_inner():
            print('my name is %s' % name)
            fun_name()

        return fun_inner_inner

    return fun_inner

@fun('大熊')
def index1():
    print('执行index函数')

@fun('小熊')
def index2():
    print('执行index函数')

index1()
print('------------------')
index2()








