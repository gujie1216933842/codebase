class Person(object):
    __slots__ = ('name', 'age') #限制person类只能设置name和age两个属性
p = Person()
p.name = 'haha1'
print(p.name)

