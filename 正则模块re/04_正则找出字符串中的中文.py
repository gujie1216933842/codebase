import re
ch_str = '哈你哈哈哈发送sfefse发射发送'

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

ret = re.findall(zh_pattern,ch_str)
print(ret)


print(re.sub(zh_pattern,'english',ch_str))

'''
python中字符串替换replace和re.sub的区别
sub用到re正则库,可以用正则查找出来,并且替换
而replace 是简单的字符串的替换,效率更高
而sub可以用正则查找,功能更强

'''