print(0.10 + 0.20)

print(round(0.10+0.21,2))

'''
0.30000000000000004
出现上面的情况，主要还是因浮点数在计算机中实际是以二进制保存的，有些数不精确。

round()函数 方法返回浮点数x的四舍五入值。
如果最后为0的会舍去

'''

from decimal import Decimal
print(Decimal(0.10)+Decimal(0.20))


rate = 0.2
print("分类正确率是：%.3f%%" % (rate * 100))   #20.000%
print("分类正确率是：%.2f%%" % (rate * 100))   #20.00%

