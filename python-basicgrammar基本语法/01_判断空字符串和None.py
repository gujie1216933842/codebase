'''
在Python中，
    None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。
    除此之外的其它对象都会被转化成True。

'''

a1 = ''
if not a1:
    print("a1")

a2 = ()
if not a2:
    print("a2")

a3 = []
if not a3:
    print("a3")

a4 = {}
if not a4:
    print("a4")

a5 = None
if not a5:
    print("a5")


print('************开始区分None和空字符串*****************')
a6 = None
if a6 is None :
    print("a6")

a7 = ''
if a7 is None:
    print('a7')


