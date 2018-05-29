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

rabbitmq-server start



'''