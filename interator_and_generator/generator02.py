'''
yield单线程异步并发实现

yield 打破了常规的代码执行顺序,甚至跳出循环,而且限次调用函数(生成器)时还可以接着上次代码向下执行
接下来的代码具体展示yield特性有什么用
'''

import time
'''
生产者消费者模型
'''

def consumer(name):    #生成器
    print('%s准备吃烧烤啦' % name)
    while True:
        shaokao = yield
        print('烧烤%s被%s吃了!' % (shaokao, name))

def producter():
    c = consumer("A")
    c1 = consumer("B")
    c.__next__()
    c1.__next__()
    print("开始生火烤串啦!")
    for i in range(3):
        time.sleep(1)
        print('烤了两串羊肉')
        c.send(i)
        c1.send(i)

producter()
'''
 这里就实现了异步并发控制，一个函数和生成器之间调用，通过yield实现；
 这里面还有个知识点，c.send(i)，前面讲过yield不仅能返回值，
 而且还能接收值，在这里send()大家可以理解为与next()一样，都是触发调用生成器中的代码，
 但next()可以理解为传一个空值给yield，send()则可传一个实际的值给yield。
 以上代码中将i值传给了生成器consumer中的Yield
'''
