'''
正则实战
search()方法和match()方法的区别
正则表达式都是从左往右开始匹配,match()从开头匹配,而search()是从左往右第一次出现,则匹配成功


'''
import re

''' 匹配处0-100之间的整数'''
pattern = r'[1-9]\d?$|0$|100$'  # 把0和100单独考虑
pattern1 = r'[1-9]?\d?$|100$'  # 优化,把0兼容
pattern2 = r'[1-9]?\d?0?$'  # 优化1,把100兼容

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
ret3 = re.match(pattern3, '10000000')
print(ret3)

'''匹配大于等于0整数'''
pattern4 = r'[1-9]\d*$|0$'
ret4 = re.match(pattern4, '0')
print(ret4)

'''匹配手机号码'''
pattern5 = r'1[3,4,5,7,8]\d{9}$'     #/^1[3,4,5,7,8][0-9]{9}$
ret5 = re.match(pattern5, '13585591803')
print('pattern5:%s' % ret5)

'''匹配空白(空格和tab键)'''
pattern6 = r'\s'
ret6 = re.match(pattern6, ' ')
print('pattern6:%s' % ret6)


'''匹配邮箱
@之前必须有内容且只能是字母（大小写）、数字、下划线(_)、减号（-）、点（.）
@和最后一个点（.）之间必须有内容且只能是字母（大小写）、数字、点（.）、减号（-），且两个点不能挨着
最后一个点（.）之后必须有内容且内容只能是字母（大小写）、数字且长度为大于等于2个字节，小于等于6个字节

'''
pattern7 = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$'
ret7 = re.match(pattern7, 'gujientsy@163.com')
print('pattern7:%s' % ret7)