a = 1
try:
    print(a)
except Exception as e:
    print(e)
else:
    print('hello')
finally:
    print(123)

'''
except:捕捉到异常
else:没有异常
finally:有没有异常都会执行
'''
