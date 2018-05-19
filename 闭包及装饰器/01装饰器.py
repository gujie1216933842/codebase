#Author:Bob

def check_login(login_status = 0):
    def inner():
        if not login_status:
            print("请先登录")
        else:
            print("已登录")
    return inner() #inner()一定要加括号


a = check_login(0)




