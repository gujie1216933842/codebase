'''yield'''


def foo(x):
    for i in range(x):
        a = yield i + 1
        yield a
        yield i


'''
函数foo数一个生成器对象,即a就是一个生成器对象
遇到yield暂停,遇到next()或者send()方法重新触发程序



'''
a = foo(5)

print(next(a))
print(next(a))
a.send(12)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

'''yield from'''


def foo2(x):
    for i in range(x):
        yield i


c = foo2(5)
print(c)
for i in c:
    print(i)

'''yield from'''


def foo1(x):
    yield from range(x)


b = foo1(5)
print(b)
for i in b:
    print(i)

''''
yield from iterable_obj 
等价于
for i in iterable_obj:
     yield i


'''
