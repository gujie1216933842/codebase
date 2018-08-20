'''
range:生成的是一个列表
xrange:生成的是一个生成器,注意:python3中,取消了xrange
当数据不多时,两个作用一样,当时数据量很大,需要生成很大的数字序列,就需要用到xrange
'''

for i in range(5):
    print('range{}'.format(i))


# print(xrange(5))
