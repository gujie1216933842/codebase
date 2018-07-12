import numpy as npy
import os
import pandas as pda
import matplotlib.pylab as pyl

'''
解决可视化的问题
绘制折线图
'''

file_path = os.path.join(os.path.dirname(__file__), 'dd.csv')
fn = open(file_path)
ret = pda.read_csv(fn)

# print(ret.describe())

# 按照某一列排序
# ret = ret.sort_values(by='price')
# print(ret)


x = [1, 2, 3, 4, 7]
y = [5, 7, 2, 1, 5]
# 绘制折线图
pyl.plot(x, y)
pyl.show()

# 绘制散点图
pyl.plot(x, y, 'o')
pyl.show()

# 设置为品红
pyl.plot(x, y, 'm')
pyl.show()
'''
c-cyan  青色
r-red   红色
m-magente  品红
g-green  绿色
b-blue   蓝色
y-yellow 黄色
b-black  黑色
w-white  白色

'''

#散点和颜色一起使用
pyl.plot(x, y, 'mo')
pyl.show()


'''
线条样式
-   直线
--  虚线
-.  线型号
:   细小虚线

'''
pyl.plot(x, y, ':')
pyl.show()


'''
点的形式
s  方形
h  六角形
H  六角形
*  星型
+  加好
x  x型
d  菱形
D  菱形
p  五角形

'''
pyl.plot(x, y, 'p') #此时已默认是散点图了
pyl.title('haha')
pyl.ylabel('yzhou')
pyl.xlabel('xzhou')
pyl.xlim(1,20)  #横轴的范围
pyl.ylim(1,20)  #纵轴的范围
pyl.show()


'''
在同一个图中绘制多条线段
'''
