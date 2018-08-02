
fun =  lambda x, y: x*y  #函数输入是x和y，输出是它们的积x*y

x = lambda x: x + 1
print(x(1))

import time

'''匿名函数没加参数'''
now = lambda: time.time()
print(now())

'''map函数'''
li = [1, 2, 3]
new_list = map(lambda x: x + 1, li)
print(new_list) #python2
print(list(new_list)) #python3
