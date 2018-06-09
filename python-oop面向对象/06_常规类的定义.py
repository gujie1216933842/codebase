class A(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
'''
__init__()方法有两个作用:
1.python对象生命周期的第一步
2.用来传递类实例化需要的参数变量
'''

a = A('daxiong').getName()
print(a)