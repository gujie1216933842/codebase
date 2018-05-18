__author__ = 'gujie'

'''
__hash__ 对应hash()方法   如果是字符串,返回对应的hash值,并且每次返回不同,如果是整型,则返回它自己
__str__ 对应的str()方法

关于控制参数访问的__getattr__, __setattr__, __delattr__, __getattribute__:

__getattr__ 是一旦我们尝试访问对象的一个并不存在的属性就会调用,二如果这个属性存在,则不会调用


'''
