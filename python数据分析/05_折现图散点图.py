import numpy as np

import pandas as pda
import matplotlib
'''
解决可视化的问题
'''


ret = pda.read_csv("C:/Users/Administrator/Desktop/qq/dd.csv",encoding = 'gbk')

print(ret.describe())

#按照某一列排序
ret = ret.sort_values(by='price')
print(ret)








