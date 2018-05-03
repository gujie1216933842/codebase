# a = "  asdada   "
# print(a.lstrip())
# print(a.rstrip())
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = a+1, b+1
        n = n + 1
    return a    
# f=fab3(5)
# print(f) 
# print('fab3 return a iterable obj ,used by for ')
# for n in f:
#     print(n)

#yield from iterable本质上等于for item in iterable: yield item的缩写版 

#函数中有了yield a 表示 调用该函数返回的是一个迭代器(可以遍历的对象 ,a 表示遍历后的item)

def fun2(m):
	a = 1
	yield a
	return 5
	
b = fun2(5)

yield from b

# print(b)

# for x in b:
# 	print(x)


