'''
需求:一个列表,把列表中的每一个元素都加1
'''
#方法一
a = [1,2,3]
b = enumerate(a)
# for k,v in b:
#     a[k] = v+1
# print(a)


#方法二
#生成器

a = [ i+1 for i in a ]

print(a)








