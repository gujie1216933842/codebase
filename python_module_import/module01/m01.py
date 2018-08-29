from module02 import m02

a2 = m02.A2()
res = a2.get_name()
print(res)


from module01 import n01
n = n01.B1()
print(n.get_name())

import n01
nn = n01.B1()
print(nn.get_name())


class A1():
    def get_name(self):
        return 'm1'
