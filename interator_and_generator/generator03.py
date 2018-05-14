def fun1():
    yield
    return  1

a = fun1()   #生成器对象
print(a.__next__())
print(a.__iter__)

