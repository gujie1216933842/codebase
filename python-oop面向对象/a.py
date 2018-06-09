#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-04-24 23:07:26
# @Last Modified by:   anchen
# @Last Modified time: 2018-04-25 00:52:33


def func1(*args,**kwargs):
    print(args,kwargs)

class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print('calling normal_method',args,kwargs)
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})") 
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})") 
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})") 
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})") 
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})") 
        return self._some_other_property


# o = MyClass()
# o.normal_method
# o.normal_method()     
# o.normal_method(1,2,x=3,y=4)


# o.class_method
# o.class_method()
# o.class_method(1,2,x=3,y=4)

# o.static_method
# o.static_method()

'''
深拷贝和浅拷贝
'''
import copy
a = [11,121,[1,3]]
b = a
a_copy = copy.copy(a)
a_deep_copy = copy.deepcopy(a)

# a_site = id(a)
# a_c_site = id(a_copy)
# a_dc_site = id(a_deep_copy)

# print(a_site)
# print(a_c_site)
# print(a_dc_site)

# print(a_copy==a_deep_copy)
# print(a_copy is a_copy)

a[2][0] = "ad"
a[0] = "asdf"
print(a)
print(b)
print(a_copy)
print(a_deep_copy)

'''
列表 a = [11,121,[1,3]] ,在内存中会开辟区域存放三个元素 11,121,[1,3]的内存地址
       11,121,[1,3] 也会开辟内存存放三个元素

赋值:  a[2][0] = "ad"
       a[0] = "asdf"     把a[2][0],a[0]存放的内存地址都替换成新的元素 
       b随着a会同时一起改变


       浅拷贝:只赋值了第一层的内存地址,第二层以上的,不会变,
            所以a第二层以上的元素赋值有变化,a_copy也会跟着一起变化

       深拷贝:内存地址全部赋值,已经开辟了一块新的值,无论原来a如何变化,  a_deep_copy都不会变化  
'''











