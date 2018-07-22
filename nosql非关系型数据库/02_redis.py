'''
redis中的数据类型
String
Hash
List
Set
Sorted set
pub/sub
Transactions

'''


'''
设置有效时间     expire key second
查看值是否存在   exists key   返回 1 或 0
查看键的有效时间   ttl key
查看类型    type key

'''

'''
hash类型  
hash用于存储对象,对象格式为{属性:值}对

对象:
{
  name:大雄
  age:33
}


设置值
hset gujie name '大雄'
取值
hget  key  field

获取对象的所有属性
hgetall gujie  


获取所有的key
hkeys key

获取所有的值
hvals key

获取所有属性的个数
hlen key

删除属性

hdel key attr

'''


'''
list类型
插入(头部)
lpush key value1 value2

插入(尾部)
rpush key value1 value2

在一个元素前或后插入元素

linsert  key  before / after  已知的value  插入的value


获取(从list中拿掉,就没有了)类似队列的方式
rpop key  右侧拿

lpop key  左侧拿


lrange list_name  0 -1   查看列表内的所有元素


'''

'''
set类型数据 (无序)
添加数据
sadd key value1 value2 value3

查看
smembers key

'''

'''
zset 有序集合 (sorted set)
元素为string类型
元素具有唯一性,不重复
每个元素都会有一个double类型的score ,表示权重

设置

zadd key  score1 value1  score2 value2

zrange key score1 score2 (score1开始权重,score2结束权重)

'''

'''
redis发布订阅
客户端: subscribe pyll   订阅频道

服务端: publish  py11 hello  向订阅频道里添加消息,客户端能自动接收   
'''





