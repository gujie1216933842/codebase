a = dict(name='gujie', age=dict(age=33))
# a.clear()
print(a)

'''copy()方法是浅拷贝'''
b = a.copy()
b['age']['age'] = 88
print(a)

'''深拷贝'''
import copy

c = copy.deepcopy(a)
c['age']['age'] = 55
print(a)

# formkeys 将可迭代的对象转化成dict
list_a = ['a', 'b']
new_dict = dict.fromkeys(list_a, (11, 33))
print(new_dict)

b = {}
value = b.get('aa', 'bb')
print(b)
print(value)

for key, value in new_dict.items():
    print(key, value)


'''setdefault方法:根据key:a 取value,如果能取出,返回value,如果原dict中取不到,则k,v设置,返回第二个参数value'''
de = new_dict.setdefault('a','你好')
print(de)


'''update()方法:参数为可迭代对象'''
new_dict.update(cc=12,dd=88)
print(new_dict)


new_dict.update(['kk','dd'])  #注意,这里只能是两个长度的字符串,便于键值切分
print(new_dict)


new_dict.update(('vv','gg'))
print(new_dict)