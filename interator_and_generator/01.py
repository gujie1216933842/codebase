#Author:Bob
'''
生成器
创建generator的方法
'''

list_01 = [ x*x for x in range(10) ]
print(list_01)       #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(list_01))   #<class 'list'>


tuple_01 = ( x*x for x in range(10))
#print(tuple_01)       #<generator object <genexpr> at 0x0089F300>
#print(type(tuple_01))  #<class 'generator'>
# print(next(tuple_01))
# print(next(tuple_01))
# print(next(tuple_01))
# print(next(tuple_01))


#以上重复调用的方法不是很好,最好用for 来循环

for i in tuple_01:
    print(i)






