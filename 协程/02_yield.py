'''
含有yield的函数,称为生成器函数,
obj = fun()    obj表示一个生成器对象,注意:此时并不执行函数
next(obj)    调用生成器对象的next()方法,  此时函数的中yield有return的作用,还会记住这一次的断点状态,
             遇到下一个yield的时候,接着上次记住的状态接着往下执行

'''

def fun(a):
    b = 0
    while a > 1:
        a -= 1
        b = yield a
        yield b
    return b
bb = fun(5)
print(next(bb))
print('aa%s'%(bb.send('hhhhh')))
print(next(bb))
print(next(bb))

'''
a = 5
a = 4
yield a   返回 a = 4,函数程序中断,等待生成器下次调用next()方法


在断点出设为断点值 'hhhhh'  ,赋值给b

yield b  第二次调用断点  返回 b的值









'''