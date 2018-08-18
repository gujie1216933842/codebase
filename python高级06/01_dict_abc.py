'''dict属于map类型'''

from collections.abc import Mapping,MutableMapping

a = {}
print(isinstance(a,MutableMapping))
'''a不是继承muttablemapping,而是实现了里面定义的某些魔法函数'''
