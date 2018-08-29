from module02 import m02
import sys

a2 = m02.A2()
res = a2.get_name()
print(res)

from module01 import n01
print(n01.a_str)
n = n01.B1()
print(n.get_name())

import n01
print(n01.a_str)


class A1():
    def get_name(self):
        return 'm1'
