import  copy
a = 123
b = a
print(id(b))
a = 124
print(id(b))


print('***********************')


a1 = 222
b1 = copy.copy(a1)
print()