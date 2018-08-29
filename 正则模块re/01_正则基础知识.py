'''
re模块式python解释器中提供了一些关于正则的工具
正则表达式中的单字符匹配
.   匹配任意一个字符,除了(\n)
\d  匹配数字
\D  匹配非数字
\s  匹配空白,即空格,tab键
\S  匹配非空白
\w  匹配单词字符  即a-z,A-Z,0-9,_
\W  匹配非单词字符

[]  方括号
正则模块re.match('1[abcd]','1a')     能匹配  1a 1b 1c 1d
等价于
正则模块re.match('1[a-d]','1a')      能匹配  1a 1b 1c 1d
取相反
正则模块re.match('1[^a-d]',1a)       能匹配除了 1a 1b 1c 1d之外  比如 1e


所以
[0-9] <=>等价于  \d
[^0-9] <=>等价于  \D

[a-zA-Z0-9_] <=>等价于  \w
'''

'''
表示数量
匹配多个字符相关的格式
*      匹配前一个字符出现0次后者无限次,即前一个字符可有可无
       正则模块re.match('\d*','123') 可以匹配
+      匹配前一个字符出现1次或者n次,即出现至少1次
?      匹配前一个字符出现1次或者0次,要么有1次,要么没有
{m}    匹配前一个字符出现m次
{m,}   匹配前一个字符至少出现m次
{m,n}  匹配前一个字符出现m到n次
'''

'''
需要匹配的字符串有转义字符   \\nw
r''    写正则表达式的时候都需要加上r,原始字符串,让我们忽略掉需要转义的地方

'''

'''
表示边界
^     匹配字符串开头         在match方法中^作用不是很明显
$     匹配字符串结尾
\b    匹配一个单词的边界
\B    匹配非单词边界      正则模块re.match('\bve\b','hove')   

'''

'''
一、模式串匹配
前几天了解到正则语法和有穷自动机的等价性，因此特意来复习一下RE的基本用法（太久没用了，手生）。
日常来说，正则表达式的主要方法是re.method()这样的模式串匹配，一共有四种常用方法：

1、match
re.match(pattern, string[, flags])  

从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，
若要完全匹配，pattern要以$结尾。

2、search
re.search(pattern, string[, flags])  
若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，
只返回第一个。

3、findall
re.findall(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为数组。

4、finditer
re.finditer(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。

'''


import re

pattern = "gujie1"  #校验规则,可以使string,或者是正则表达式
string = "gujie hahah"
result = re.match(pattern, string)
#result 属于  Match对象

print(result)  #

# ret = result.group()
# print(ret)  #gujie

res = re.match('1[35678]\d{9}',"")

