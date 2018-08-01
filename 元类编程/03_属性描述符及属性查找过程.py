'''
如果user是某个类的实例,那么user.age以及(等价的getattr(user,'age'))

首先调用__getattribute__,如果定义了__getattr__方法
哪个在__getattribute__跑出attributeError的时候就会调用到__getattr__

而对于描述符(__get__)的调用,则是发生在__getattributte__内部的.

user = User()  user.age顺序如下:

1.如果'age'是出现在User或者其基类的__dict__中,且age是data desccriptor,那么调用其

2.如果'age'出现在实例obj(user)的__dict__中,那么直接返回obj.__dict__['age'],否则

3.如果'age'出现在User或者其基类的__dict__中

    3.1. 如果age是non-data descriptor,那么调用其__get__方法,否则
    3.2. 返回__dict__['age']
4.如果User有__getattr__方法,调用__getattr__方法,否则

5.抛出AttributeError





'''

from datetime import date


class User():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return 'none attr'

    # def __getattribute__(self, item):
    #     print('in getattibute')

    def __get__(self, instance, owner):
        print('in get ')



if __name__ == "__main__":
    user = User('tom', date(year=1990, month=11, day=7))
    print(user.age)
    user.age = 100
    print(user.__dict__)