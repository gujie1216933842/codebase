'''
字符串的操作
'''

#替换字符串中等的字符
#replace(捞取字符,修改成的字符,修改次数)第一个参数可用正则
str = 'abcdsabsffrsr3sfes'
newstr = str.replace('ab','666',1)   #第三个参数,表示原字符串从左往右能被替换的次数,默认是全部替换
print(newstr)


#re.sub(捞取字符,修改成的字符,原整个字符串,修改次数) ,三个参数必填
#先导入re
import re
str2 = re.sub('a','','aaab',2)
print(str2)
print('---------------------------------')


#strip() 移除字符串中的字符
str3 = 'hahahahah'
print(str3.strip('x'))   #方法用于移除字符串头尾指定的字符（默认为空格或换行符）
print(str3.lstrip('h'))    #移除头
print(str3.rstrip('h'))    #移除尾

print('--------------------------------')

#字符串变成列表
str4 = 'hello'
print(list(str4))
str5 = 'h-e-l-l-o'
#字符串拆分,也有字符串变成列表的作用
print(str5.split('-'))

#列表变成字符串
a = ['a','b','c']  #注意:如果用join的话,列表中元素只能是字符串类型
print('-'.join(a))

#这里也能实现往字符串中插入字符
print('-'.join('aaaaa'))







