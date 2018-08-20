'''
@classmethod和@staticmethod是python中定义方法的修饰方式

common function 需要实例化才能调用
staticmethod修饰的方法:可以直接用类名调用,实例化之后也可 , 不需要self 作为类方法的第一参数
classmethod修饰的方法:可以直接用类名调用,实例化之后也可 , 类方法的第一参数用cls


'''


class A(object):
    def foo(self, x):
        print('common function:{}'.format(x))

    @staticmethod
    def static_foo(x):
        print('static function:{}'.format(x))

    @classmethod
    def class_foo(cls, x):
        print('class_method:{}'.format(x))


A.class_foo(3)

A.static_foo(6)

A().foo(5)
A().class_foo(5)
A().static_foo(5)
