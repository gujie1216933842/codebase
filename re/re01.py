'''
re模块式python解释器中提供了一些关于正则的工具
正则表达式中的单字符匹配
.  匹配任意一个字符,除了(/n)
\d  匹配数字
\D  匹配非数字
\s  匹配空白,即空格,tab键
\S  匹配非空白
\w  匹配单词字符  即a-z,A-Z,0-9
\W  匹配非单词字符
'''

import re

pattern = "gujie1"  #校验规则,可以使string,或者是正则表达式
string = "gujie hahah"
result = re.match(pattern, string)
#result 属于  Match对象

print(result)  #

# ret = result.group()
# print(ret)  #gujie

