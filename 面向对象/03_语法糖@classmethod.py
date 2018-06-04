'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：

总结:普通类方法,@classmethod类方法,@staticmethod类方法区别比较
首先方法书写形式(这里没考虑有参数,如果有参数,一次往后加)
普通:            fun(self):
@classmethod:    fun(cls)
@staticmethod:   fun()




'''


class Student(object):
    name = 'haha'
    def __init__(self,name): #init方法中的变量设置时实例时候用的
        self.name = name

    @classmethod
    def getName(cls):
        return cls.name


s = Student('你好')
print(s.getName())

print(Student.getName())

