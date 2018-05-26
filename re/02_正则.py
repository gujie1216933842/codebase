'''
正则实战
search()方法和match()方法的区别
正则表达式都是从左往右开始匹配,match()从开头匹配,而search()是从左往右第一次出现,则匹配成功


'''
import re

''' 匹配处0-100之间的整数'''
parttern = r'\d'
ret = re.match(parttern, "9a8")
print(ret)

if ret:
    print(True)

ret2 = re.search(parttern,'a6j9')
print(ret2)