
def check_login(fun):
    def inner():
        print("正在验证权限.....")
        fun()
    return inner


def index():
    print("展示index页面")

a = check_login(index)
a()

















def a():
    return 1

# print(a)  # 不带括号调用的结果：<function a at 0x1091766a8>
# print(a())  # 带括号调用的结果：3
