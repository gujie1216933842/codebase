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


import copy
a = [11,121,[1,3]]

a_copy = copy.copy(a)
a_deep_copy = copy.deepcopy(a)

a_site = id(a)
a_c_site = id(a_copy)
a_dc_site = id(a_deep_copy)

print(a_site)
print(a_c_site)
print(a_dc_site)

print(a_copy==a_deep_copy)
print(a_copy is a_copy)

a[2] = "ad"
print(a_copy)
print(a_deep_copy)


