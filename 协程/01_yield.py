'''
含有yield的函数,称为生成器函数,
obj = fun()    obj表示一个生成器对象,注意:此时并不执行函数
next(obj)    调用生成器对象的next()方法,  此时函数的中yield有return的作用,还会记住这一次的断点状态,
             遇到下一个yield的时候,接着上次记住的状态接着往下执行


yield:  生成器函数运行遇到yield关键字,中断程序,并且记住断点状态,等待生成器对象被调用next()或者send()激活
next()和send()是恢复中断的生成器函数
通过 go和stop两个开关来实现程序的异步

'''

def fun(a):
    b = 0
    while a > 1:
        a -= 1
        b = yield a  #注意:yield表达式可以接收send()发出的参数,如果上一步没有send()方法,则b为None
        yield b
    return b
bb = fun(5)
print(next(bb))
print('aa%s'%(bb.send('hhhhh')))
print(next(bb))
print(next(bb))
print(next(bb))
print(next(bb))

'''
a = 5
a = 4

yield a   返回 a = 4,函数程序中断,等待生成器下次调用next()或者send()方法激活

bb.send('hhhhh')  第1次激活生成器
yield b  再次中断  此时应为b有有断点赋值  所以返回 hhhhh

在断点处设断点值 'hhhhh'  ,也会返回生成器的值   hhhhh  再次中断

第3次激活  遇到yield a 返回a = 3  中断

第4次激活  遇到yield b 上一步没有send()赋值,所以返回None



yield b  第二次调用断点  返回 b的值









'''