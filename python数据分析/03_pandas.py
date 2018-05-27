import numpy as np

import pandas as pda

# 创建数组(一维数组)
'''
两种新的数据类型
series       一行或者一列
dataframe    几行几列

'''
# 如果不指定索引,默认从0开始排下去
np1 = pda.Series([4, 5, 4, 5, 6, 6])
print(np1)
# 指定索引
np2 = pda.Series([4, 3, 2, 5], index=[3, 4, 'se', 3])
print(np2)

# 创建数据框,如果元素不存在,以NaN自动补全
np3 = pda.DataFrame([[1, 2], [2, 3,5    ], ['11']])
print(np3)


#可以自定义列名
np4 = pda.DataFrame([[1, 2], [2, 3,5    ], ['11']],columns=['qq','bb','cc'])
print(np4)

print(np4.head(1)) #,取指定的前几行,默认取前5行
print(np4.tail(1)) #,取指定的尾部几行,默认取尾部5行


#展示所有数据的展示情况
print(np4.describe())  #以列统计

#  mean 这一列的平均数
#  std  这一列数据的标准差
#  25%/50%  这一类的数据的分位数 前分位数/中分位数/后分位数


#数据框行列转置
print(np4.T)


