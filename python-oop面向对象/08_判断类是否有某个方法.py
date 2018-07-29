class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['aa', 'bb', 'cc'])
print(hasattr(com, '__len__'))

# 在某些情况下希望判定某个对象的类型
from collections.abc import Sized

print(isinstance(com, Sized))


# 我们需要强制某个子类必须是想某些方法
# 比如实现了一个web框架,集成cache(redis,memcache)
# 需要设计一个抽象基类,指定子类必须实现某些方法


class CacheBase():
    def get(self, key):
        pass

    def set(self, key, value):
        pass
