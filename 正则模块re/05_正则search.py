import re

'''匹配正整数'''
pattern3 = r'[1-9]\d*$'
ret3 = re.search(pattern3, 'a10000000')
print(ret3)

ret4 = re.match(pattern3, '10000000')
print(ret4)




'''
match（）函数只检测RE是不是在string的开始位置匹配， search()会扫描整个string查找匹配, 
也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none

例如：

print(re.match(‘super’, ‘superstition’).span())会返回(0, 5)
而print(re.match(‘super’, ‘insuperable’))则返回None

search()会扫描整个字符串并返回第一个成功的匹配

例如：print(re.search(‘super’, ‘superstition’).span())返回(0, 5)

print(re.search(‘super’, ‘insuperable’).span())返回(2, 7)


'''