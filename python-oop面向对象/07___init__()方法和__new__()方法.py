'''
在实例化的过程中
会先调用__new__方法
然后才会调用__init__方法
https://www.cnblogs.com/nyist-xsk/p/8286941.html

'''


class A(object):
    '''
    注意:一般情况下,不重写__new__方法
    '''
    def __new__(cls, *args, **kwargs):
        print('调用new方法')
        return object.__new__(cls)

    def __init__(self, name, age):
        print('调用init方法')
        self.name = name
        self.age = age

    def get(self):
        print('hahaha')
        print(self.__class__)


if __name__ == '__main__':
    a = A('jj', 34)
    a.get()
    print(a.__class__)