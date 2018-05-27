import numpy as np

import pandas as pda

# 创建数组(一维数组)
'''
两种新的数据类型
series       一行或者一列
dataframe    几行几列

'''
#如果不指定索引,默认从0开始排下去
np1 = pda.Series([4,5,4,5,6,6])
print(np1)
#指定索引
np2 = pda.Series([4,3,2,5],index=[3,4,'se',3])
print(np2)





