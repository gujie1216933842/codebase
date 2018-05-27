import numpy as np
import os
import pandas as pda
import matplotlib

'''
解决可视化的问题
绘制折线图
'''

file_path = os.path.join(os.path.dirname(__file__), 'dd.csv')
fn = open(file_path)
ret = pda.read_csv(fn)

'''
注:因为这里的文件路径存在中文,所以先打卡文件在读取,实际开发中的文件路径不能存在中文,所以可直接读取
ret = pda.read_csv(f,encoding = 'gb18030')   #gbk也可
'''
#


print(ret.describe())

# 按照某一列排序
ret = ret.sort_values(by='price')
print(ret)
