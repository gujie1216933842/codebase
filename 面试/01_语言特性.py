'''
1.python的函数传递

2.python中的元类(metaclass)


3.@classmethod和@staticmethod
 classmethod :类方法,第一参数cls
 staticmethod: 静态方法,无第一参数
 都不需要类的实例化,类名直接调用

4.类变量和实例变量
 类变量:也成为静态变量,也就是在变量前加了static的变量
 实例变量:也叫对象变量,即没有加static的变量,
 区别在于:类变量是所有对象共有的,其中一个对象将它的值改变,其他对象得到的值就是改变后的结果
         实例变量则属于对象私有,某一个对象将其值改变,不影响其对象中的值


5.Python自省


6.字典推导式
 (字典推导式):
    mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
    mcase_frequency = {
        k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
        for k in mcase.keys()
        if k.lower() in ['a','b']
    }

7.python中双下划线和单下划线(__xxx和_xxx)
 __xxx  双下划线,类的私有变量                 private
 _xxx   单下划线,不能用 from 模块 import xxx  protect


8.字符串格式化:%和.format
 mystr = 'aaaa:%s'%('bb')
 mystr = 'aaaa:{}'.formate('bb')

9.迭代器和生成器
 生成器:
        a  函数中有yield关键字
        b  iter([1,2,3,4])
 迭代器: python对象实现了__next__方法和__iter__方法

 生成器只能生成一次
 生成器是迭代器的一种


10.*args and **kwargs
 *args:作为参数,打印出来以元组的形式展示
 **kwargs:作为参数,打印出来以字典的形式展示
 注意点：普通参数、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。



'''


