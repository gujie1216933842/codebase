'''
python代码实现删除列表中的重复元素
思路:把列表中的值作为字典的key值转化为字典
     再把转换后的字典转换成列表
     fromkeys(a)方法:把列表a转换成字典中的key值,因为字典中的key有唯一性,所以又去重作用
'''
def function(a):
    b = dict()
    keys = b.fromkeys(a)
    c= list(keys)
    print(c)

function([1,1,3,3,3,8,4,5])
print("我爱你")


'''
列表排序
'''

a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
a.sort()
function(a)








