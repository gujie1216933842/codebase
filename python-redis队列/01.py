'''
http://ju.outofmemory.cn/entry/108351


https://www.cnblogs.com/arkenstone/p/7813551.html

https://blog.csdn.net/Neleuska/article/details/80040304  这条参考价值较大

'''


'''
redis设置密码
[root@hadoop4 redis-3.2.4]# cd src/
[root@hadoop4 src]# ./redis-cli 
127.0.0.1:6379> config set requirepass 123
OK
127.0.0.1:6379> quit

[root@hadoop4 src]# ./redis-cli 
127.0.0.1:6379> auth 123
OK
127.0.0.1:6379> 

以上是方法,在重启redis服务后,设置密码会失效
如果想永久设置redis密码,需要在redis.conf文件中做设置
加上这段代码
reqiurepass 123 


'''