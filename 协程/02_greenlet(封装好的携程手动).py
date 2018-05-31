from greenlet import greenlet

'''
greenlet是手动切换协程

'''


def fun1():
    print(12)
    gr2.switch()
    print(13)
    gr2.switch()


def fun2():
    print(14)
    gr1.switch()
    print(15)


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()
