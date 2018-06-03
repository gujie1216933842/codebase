'''
正则实战
search()方法和match()方法的区别
正则表达式都是从左往右开始匹配,match()从开头匹配,而search()是从左往右第一次出现,则匹配成功


'''
import re

''' 匹配处0-100之间的整数'''
pattern = r'[1-9]\d?$|0$|100$' #把0和100单独考虑
pattern1 = r'[1-9]?\d?$|100$'  #优化,把0兼容
pattern2 = r'[1-9]?\d?0?$'     #优化1,把100兼容

'''
分析:\d后面加问号的原因是要兼容个人整数
|  竖线是或者的意思
$  符号是结束边界
'''


ret = re.match(pattern2, "99")
print(ret)

# if ret:
#     print(True)
#
# ret2 = 正则模块re.search(pattern,'a6j9')
# print(ret2)


'''匹配正整数'''
pattern3 = r'[1-9]\d*$'
ret3 = re.match(pattern3,'10000000')
print(ret3)


'''匹配大于等于0整数'''
pattern4 = r'[1-9]\d*$|0$'
ret4 = re.match(pattern4,'0')
print(ret4)






