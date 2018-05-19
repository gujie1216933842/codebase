
def check_login(fun):
    def inner():
        print("正在验证权限.....")
        fun()
    return inner


def index():
    print("展示index页面")

a = check_login(index)
a()
