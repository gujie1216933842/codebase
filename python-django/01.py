'''
https://www.cnblogs.com/linxiyue/p/4040262.html
'''


'''
引入models的定义
from app.models import  myclass
class  myclass():
     aa =  models. CharField (max_length=None)　
     bb =  models. CharField (max_length=None)　
     def __unicode__(self):
         return u'%s %s' %(aa,bb)
增
添加一行数据1
add = myclass(aa='wahaha',bb='hahawa' )
add.save() #不save无法保存到数据库
add.id #获取增加的这条数据的ID
添加一行数据2
myclass.objects.create(aa='wahaha',bb='hahawa')  # 同上1方法一样无需保存save


删
删除表中全部数据
myclass.objects.all().delete()
删除一条aa等于'test'的数据
myclass.objects.get(aa='test').delete()
删除多条数据
myclass.objects.filter(aa='123').delete() #过滤出aa字段等于123的都删除

查
查出库中所有条数的数据
myclass.objects.all()
查询带字段名的所有条数数据
myclass.objects.all().values()
查询单挑数据
myclass.objects.get(aa='123') #查询aa字段中是123的这条数据,如果是多条和没有的时候会报错,尽量结合try:except使用 
查询匹配条件的多条数据
myclass.objects.filter(aa='123') #查询aa字段值为123的所有数据条数,括号的匹配条件可多个,以逗号分隔
模糊查询
myclass.objects .filter(aa__contains="1") #查询aa字段中值包含'1'的数据,例如aa字段值为 123 154 这两条都能匹配
根据字段内容排序后展示数据
myclass.objects.order_by('aa')  #根据aa字段的内容进行数据排序,会根据字母和数字排序
根据字段内容逆向排序后展示数据,加一个负号
myclass.objects .order_by('-aa' )  #根据aa字段的内容进行逆向数据排序,会根据字母和数字排序
连锁查询,先过滤,过滤后进行逆向排序
myclass.objects.filter(aa='123') .order_by("‐aa")
限制数据条数,相当于mysql limit
myclass.objects.filter(aa='123')[0]  #[0]显示第一条 [0:2]会显示前两条
myclass.objects.filter(aa='123').order_by("‐aa")[0] #切片不支持负数,这样就数据序列倒过来的第一条,也就是最后一条数据 

改
更新数据
a = userinfo.objects.get(cellPhone='13133333333') #查询一条你要更新的数据
a.cellPhone='3111111111111'   #赋值给你要更新的字段
a.save() #保存
更新多个字段或一个字段
myclass.objects .get(aa='123').update(aa='321',bb="wahaha") #update可多条
更新所有字段
myclass.objects.all().update(aa='8888') #更新所有字段,更新后会显示受影响的条数



'''