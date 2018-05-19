'''闭包小实例'''
def fun1(a, b):
    def fun2():
        print(a + b)

    return fun2()
a = fun1(1, 3)
