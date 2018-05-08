'''
re模块式python解释器中提供了一些关于正则的工具
正则表达式中的单字符匹配
.  匹配任意一个字符,除了(/n)
\d  匹配数字
\D  匹配非数字
\s  匹配空白,即空格,tab键
\S  匹配非空白
\w  匹配单词字符  即a-z,A-Z,0-9,_
\W  匹配非单词字符

[]  方括号
re.match('1[abcd]','1a')     能匹配  1a 1b 1c 1d
等价于
re.match('1[a-d]','1a')      能匹配  1a 1b 1c 1d
取相反
re.match('1[^a-d]',1a)       能匹配除了 1a 1b 1c 1d之外  比如 1e


所以
[0-9] <=>等价于  \d
[^0-9] <=>等价于  \D

[a-zA-Z0-9_] <=>等价于  \w
'''

'''
表示数量
匹配多个字符相关的格式
*      匹配前一个字符出现0次后者无限次,即前一个字符可有可无
       re.match('\d*','123') 可以匹配
+      匹配前一个字符出现1次后者n次,即出现至少1次
?      匹配前一个字符出现1次后者0次,要么有1次,要么没有
{m}    匹配前一个字符出现m次
{m.}   匹配前一个字符至少出现m次
{m,n}  匹配前一个字符出现m到n次



'''



import re

pattern = "gujie1"  #校验规则,可以使string,或者是正则表达式
string = "gujie hahah"
result = re.match(pattern, string)
#result 属于  Match对象

print(result)  #

# ret = result.group()
# print(ret)  #gujie

