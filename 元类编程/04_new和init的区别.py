'''
new 是用来控制对象的生成过程,在对象生成之前
init 是用来完善对象的
如果new 方法不返回对象,则不会调用init函数
'''

class User:
    def __new__(cls, *args, **kwargs):
        print('in new')

    def __init__(self,name):
        print('in init')
        self.name = name


class User1:
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    def __init__(self,name):
        print('in init')
        self.name = name



if __name__== '__main__':
    user = User('tong')
    user1 = User1('tong')
