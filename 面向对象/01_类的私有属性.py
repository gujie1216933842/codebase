class A(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


'''
类属性不让外部直接调用,把类属性设为私有
而是通过类方法调用类属性

'''
a1 = A('daxiong')
print(a1.getName())
