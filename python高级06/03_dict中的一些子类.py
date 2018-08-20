'''
不建议继承python中的基本数据结构对象dict和list
原因:python中的dict,list有些方法用c语言调用的时候,不会去调用dict类中的魔法方法,比如__setitem__()

'''

class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value*2)

my = Mydict(one=1)
print(my)

my['one'] = 1
print(my)


from collections import UserDict
