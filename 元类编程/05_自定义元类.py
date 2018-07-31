'''
什么是元类:  元类是创建类的类
类创建流程:  type -> class(对象) -> 实例对象
python中类的实例化过程,首先会寻找metaclass,通过metaclass去创建user类
去创建类对象,实例
'''



class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name = name


    def __str__(self):
        return 'user'


if __name__=='__main__':
    my_obj = User('tom')
    print(my_obj)  #如果有__str__方法,打印的就是字符串的表现形式