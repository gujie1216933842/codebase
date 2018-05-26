'''
正则实战
search()方法和match()方法的区别
正则表达式都是从左往右开始匹配,match()从开头匹配,而search()是从左往右第一次出现,则匹配成功


'''
import re

''' 匹配处0-100之间的整数'''
parttern = r'[1-9]\d?$|0$|100$' #把0和100单独考虑
parttern1 = r'[1-9]?\d?$|100$'  #优化,把0兼容
parttern2 = r'[1-9]?\d?0?$'     #优化1,把100兼容

'''
分析:\d后面加问号的原因是要兼容个人整数
|  竖线是或者的意思
$  符号是结束边界
'''


ret = re.match(parttern2, "99")
print(ret)

# if ret:
#     print(True)
#
# ret2 = re.search(parttern,'a6j9')
# print(ret2)