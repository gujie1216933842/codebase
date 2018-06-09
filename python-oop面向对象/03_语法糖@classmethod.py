'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：

总结:普通类方法,@classmethod类方法,@staticmethod类方法区别比较
1.首先方法书写形式(这里没考虑有参数,如果有参数,一次往后加)
普通:            fun(self):
@classmethod:    fun(cls)
@staticmethod:   fun()  注意:这里没有self属性


2.调用
普通类方法的这里不再说明
@classmethod类方法   可以实例化调用,也可以直接类名调用
                    注意:如果是实例化调用,涉及到实例化参数的变化,对classmethod的方法结果是没有影响的,
                    因为cls代表的类,而不是实例,cls只有类属性,即不是__init__()方法中的属性

@staticmethod类方法  可以实例化调用,也可以直接类名调用,和classmethod类似




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

