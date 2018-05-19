# Author:Bob

def check_login(login_status):
    def inner():
        if not login_status:
            print("请先登录")
        else:
            print("已登录")

    return inner()  # inner()一定要加括号


# @check_login(1)
# def index():
#     print("展示index页面")


from functools import wraps


def task_logging(taskname):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **wkargs):
            # 函数通过装饰起参数给装饰器传送参数
            print('before task', taskname)
            # 装饰器传变量给函数
            taskid = 1
            summer, funcres = func(taskid, *args, **wkargs)
            print('after task', taskid, summer)
            return funcres

        return return_wrapper

    return func_wrapper


@task_logging("test")
def testd(taskid):
    print("testd runing", taskid)
    return "task summer success eg", []


print(testd())
