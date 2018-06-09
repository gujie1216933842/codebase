'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：

'''


class Student(object):
    name = 'haha'
    def __init__(self,name): #init方法中的变量设置时实例时候用的
        self.name = name

    @staticmethod
    def getName():
        return Student.name


s = Student('你好')
print(s.getName())
print(Student.getName())

