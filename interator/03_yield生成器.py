def fun():
    for i in range(10):
        yield i


a = fun()
#用for循环来打印生成器
for i in a:
    print(i)