import numpy as np

import pandas as pda

# 创建数组(一维数组)
'''
两种新的数据类型
series       一行或者一列
dataframe    几行几列

'''
print("****************创建series数据*******************")

s1 = pda.Series([3, 4, 5, 3, 'a'])
print(s1)

print("****************创建dataframe数据*******************")
'''
clomun参数指定列名
'''
d1 = pda.DataFrame([[1, 2, 3], [4, 3, 5], ['9', 'a', 3]])
print(d1)

print("****************(字典形式)创建dataframe数据*******************")

d2 = pda.DataFrame({
    'aa': [2, 3, 4],  # 列
    'bb': [2, 3, 4],
    'cc': [5, 3, 8]})
print(d2)


print("****************dataframe数据取哪一行哪一列数据*******************")
print(d2.head(1))
print(d2.tail(1))


print("****************dataframe数据统计分析*******************")
print(d2.describe())


print("****************dataframe数据转置*******************")
print(d2.T)
