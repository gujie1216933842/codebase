import  copy
'''
理解深拷贝和浅拷贝



'''

a = 123
b = a
print(id(b))
a = 124
print(id(b))


print('***********************')


a1 = 222
b1 = copy.copy(a1)
print(id(b1))
print(id(a1))

a1 = 111
print(id(b1))


print('***********************')


a2 = 222
b2 = copy.deepcopy(a2)
print(id(b2))
print(id(a2))
a2 = 111
print(id(b2))