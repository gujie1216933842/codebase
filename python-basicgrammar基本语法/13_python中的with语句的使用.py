'''
理解:对于一个什么样的对象可以使用with语句
实现了上下文协议的对象使用with关键字
实现了上下文协议的对象称之为上下文管理器
上下文管理器的对象类中实现了__enter__,__exit__两个魔法方法


'''

'''自己写一个类,来实现对象的上下文管理器,能用with关键字'''


class MyResource():
    def __enter__(self):
        print('connet to recource')
        return self

    '''exit方法的作用:回收资源
                     处理异常
                     如果with下面的代码出现异常
                     exc_type, exc_val, exc_tb三个参数会有值
       exit方法的返回值:true:表示已经在exit方法的内部处理过了异常,如果在with外部加上try也捕捉不到
                       false:与true相反,还是能捕捉到
                    如果没有return  ,默认false'''

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('出现异常')
        else:
            print('没有异常')
        print('close connet to recource')
        return True

    def query(self):
        print('query data')


'''注意:as关键字后面不是接的不是类的实例化对象,而是__enter__()魔法方法中返回值'''
with MyResource() as resource:
    resource.query()
