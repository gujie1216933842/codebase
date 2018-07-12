import numpy as np

import pandas as pda



'''
1.导入csv数据
2.



'''

ret = pda.read_csv("C:/Users/Administrator/Desktop/qq/dd.csv",encoding = 'gbk')

print(ret.describe())

#按照某一列排序
ret = ret.sort_values(by='price')
print(ret)





