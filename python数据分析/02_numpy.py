import numpy as np

# 创建数组(一维数组)
arr1 = np.array([1, 3, 4])
print(arr1)
print(type(arr1))

# 创建二维数组(每一维的数组长度要相等)
arr2 = np.array([['xx', ''], ['ww', '44']])
print(arr2)
print(type(arr2))
# 二维数组取元素
print(arr2[1][1])

# 对数字进行排序
arr1.sort()
print(arr1)  # 字符串也比较大小

arr2.sort()
print(arr2)
# 取数组汇总的最小值,最大值
arr1.min() #这里最大值和最小值必须是整数,如果是字符串会报错

# 切片
print(arr1[1:2])  #做开右闭




