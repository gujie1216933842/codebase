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
