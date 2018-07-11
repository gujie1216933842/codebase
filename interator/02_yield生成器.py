def fun():
    for i in range(10):
        yield i


a = fun()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

'''
函数fun中含有关键字yield,fun()是一个生成器
a = fun()   a就是一个生成器对象
next(a)  触发生成器,返回一个值   0,程序中断
next(a)  触发生成器,返回一个值   1,程序中断



'''
