from datetime import date, datetime

'''
__getattr__  类调用属性,找不到调用的属性时,回去调用该魔法方法,方法里可做一些逻辑处理

__getattribute__  只要是类调用属性,就会调用到该魔法方法,一般不建议使用,把持属性调用的入口   

'''


class User():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return 'none attr'

    def __getattribute__(self, item):
        return 'get attr'


if __name__ == "__main__":
    user = User('tom', date(year=1990, month=11, day=7))
    print(user.age)
