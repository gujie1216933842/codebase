import  copy
'''
https://www.cnblogs.com/alinh/p/6603976.html

理解'='赋值和浅拷贝和深拷贝
'='     就是对象的引用(别名)
浅拷贝   拷贝父对象,不会拷贝内部的子对象
深拷贝   父对象和子对象一起拷贝


'''
print('**********"="简单赋值*************')
a = 123
b = a
print(id(b))
a = 124
print(b)


print('***********浅拷贝************')


a1 = [1,2,['a']]
b1 = copy.copy(a1)
a1[2].append(3)
print(b1)
#子对象['a']对于a1和b1公用指针地址,即a1和b1共用一个子对象['a'],其中指针最终指向的值改变了,另一个也更值改变


print('************深拷贝***********')


a2 = [1,2,['a']]
b2 = copy.copy(a2)
a1[2].append(3)
print(b2)
#a2和b2的子对象是相互独立的,是占用两个内存区域,所以其中一个子对象存储内容改变,不会另一个子对象的改变