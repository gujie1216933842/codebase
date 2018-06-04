'''
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
对属性加以访问控制，相对安全些，比如直接在__init__中定义公用属性，从封装性来说，它是不好的写法
属性之访问，它亦有机制，其一便是@propery关键字。用此关键字，其获取、设置函数，须与属性名一致

@property可以把一个实例方法变成其同名属性，以支持.号访问，它亦可标记设置限制，加以规范，如下代码：
属性可控

'''


class Student(object):
    def __init__(self,):
        self._birth = 0

    @property    #把类方法设置为类属性
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @birth.getter
    def birth(self):
        return self._birth


s = Student()
s.birth = 200
print(s.birth)

