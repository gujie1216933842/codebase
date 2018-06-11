'''
在实例化的过程中
会先调用__new__方法
然后才会调用__init__方法
https://www.cnblogs.com/nyist-xsk/p/8286941.html

'''


class A(object):
    def __new__(cls, *args, **kwargs):
        return 12

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get(self):
        print('hahaha')