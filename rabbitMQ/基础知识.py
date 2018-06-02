'''

https://blog.csdn.net/fgf00/article/details/52872730


一、RabbitMQ 消息队列介绍
二、RabbitMQ基本示例.
　　1、Rabbitmq 安装
　　2、基本示例
　　3、RabbitMQ 消息分发轮询
三、RabbitMQ 消息持久化（durable、properties）
　　1、RabbitMQ 相关命令
　　2、消息持久化
四、RabbitMQ 广播模式（exchange）
　　1、fanout 纯广播、all
　　2、direct 有选择的接收消息
　　3、topic 更细致的过滤
　　4、RabbitMQ RPC 实现（Remote procedure call）

rabbitmq和python中的queue有什么区别?
如果是两个独立的python程序,不能用两个queue进行交互
但是有一些公共的中间件可以支持,两个或者多个程序之间的交互
这些公共的中间件有一些成熟的产品:rabbitmq   zeromq  activemq

这里我们研究rabbitmq
rabbitmq是erlang语言开发
python中的rabbit模块有pika  celery  haigha



 一步启动Erlang node和Rabbit应用：./rabbitmq-server

 在后台启动Rabbit node：./rabbitmq-server -detached

 关闭整个节点（包括应用）：./rabbitmqctl stop

 rabbitmqctl list_queues  # 查看当前queue数量及queue里消息数量




'''


'''
rabbitmq安装
建议都是源码安装
1.安装erlang语言
********APPLICATIONS DISABLED*****
只剩下jinterface     : Java compiler disabled by user,可不考虑,直接下不安装


2.安装rabbitmq

复制代码
wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.5.8/rabbitmq-server-3.5.8.tar.gz
tar -zxvf rabbitmq-server-3.5.8.tar.gz
cd abbitmq-server-3.5.8
make
make TARGET_DIR=/usr/local/rabbitmq SBIN_DIR=/usr/local/rabbitmq/sbin MAN_DIR=/usr/local/rabbitmq/man DOC_INSTALL_DIR=/usr/local/rabbitmq/doc install
复制代码
配置erlang环境
vi /etc/profile #在最后添加下文
PATH=$PATH:/usr/local/erlang/bin:/usr/local/rabbitmq/sbin
使环境变量生效
source /etc/profile
3. 启动：rabbitmq-server
rabbitmq-server -detached 表示在后台启动rabbitmq服务,参考redis

rabbitmq-server start



'''


'''
 学习 使用 django+celery+RabbitMQ 实现异步执行
 https://blog.csdn.net/dipolar/article/details/22162863
 
 https://blog.csdn.net/qq415200973/article/details/42562555
 
 https://www.cnblogs.com/mysql-dba/p/6895190.html?utm_source=itdadao&utm_medium=referral
 
 http://python.jobbole.com/88276/
 
 
 
 celery常用的几个场景
 1.Web应用。当用户触发一个动作需要较长时间来执行完成时，可以把它作为任务交给celery异步执行，
   执行完再返回给用户。这点和你在前端使用ajax实现异步加载有异曲同工之妙。
 2.定时任务。假设有多台服务器，多个任务，定时任务的管理是很困难的，你要在不同电脑上写不同的crontab，而且还不好管理。
   Celery可以帮助我们快速在不同的机器设定不同任务。
 3.其他可以异步执行的任务。比如发送短信，邮件，推送消息，清理/设置缓存等。这点还是比较有用的
 
 
'''