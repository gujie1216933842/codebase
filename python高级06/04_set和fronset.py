'''
set:集合,最大的特点,无序,不重复

fronset:冻结的集合,是不可变的类型,即没有add()方法
作用:可以作为dict的key,因为我们知道dict的key必须是一个恒定的值,是不能变的
'''

myset = set(['a', 'b', 'a', 'c', 'c', 'd'])
print(myset)

'''set的一种初始化方式,注意,要和字典区分'''
s = {'a', 'b'}
print(type(s))

s.add('aa')
print(s)

'''定义一个fronset'''
myset1 = frozenset(['a', 'b', 'a', 'c', 'c', 'd'])
print(myset1)

'''set 的update的方法:可以将两个集合合并成一个集合'''

'''difference():差集'''
a_set = set('abc')
b_set = set('abvf')
diff = a_set.difference(b_set)
print(diff)
'''等价与'''
diff1 = a_set - b_set
print(diff1)

'''集合里的常用运算,对于平时我们处理数据的时候是非常有用的'''
''' |  &  -  '''
print(a_set | b_set)  # 并集
print(a_set & b_set)  # 交集
'''set的实现效率是非常高的,用的hash,时间复杂度是1'''

'''判断元素是否在集合中,   扩展:可以用in 关键字  是应为set中实现了一个魔法方法 __contains__()'''
if 'a' in a_set:
    print(True)


'''issubset 判断一个集合是否是另一个集合的子集合 '''
print(a_set.issubset(b_set))

