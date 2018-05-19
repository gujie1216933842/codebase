__author__ = 'gujie'

'''
__hash__ 对应hash()方法   如果是字符串,返回对应的hash值,并且每次返回不同,如果是整型,则返回它自己
__str__ 对应的str()方法

关于控制参数访问的__getattr__, __setattr__, __delattr__, __getattribute__:

__getattr__ 是一旦我们尝试访问对象的一个并不存在的属性就会调用,二如果这个属性存在,则不会调用


'''


class Test01(object):
    def __init__(self, world):
        self.world = world

    def __getattr__(self, item):
        return item


t1 = Test01("haha")
print(t1.__getattr__('nihao'))

b = 'aaa'


class Test02(object):
    name = "xiaoxiong"

    def run(self):
        return "hello world"

'''类方法也是属性'''
''''''
t = Test02()
flag = hasattr(t,'name')
flag1 = hasattr(t,'run')
print(flag)
print(flag1)
aa = getattr(t,"name")
print(aa)

setattr(t,'age','18')
print(t.age)












