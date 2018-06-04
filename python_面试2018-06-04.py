'''
epoll 为什么高效?
python的ioloop取询问epoll循环的时候,epoll每次返回的是真正可以处理的socket(真正可以干活的socket),
拿到有用的也是依次处理
这样,我不会把cpu时间不会浪费在无所事事的socket上了


tornado工作原理:
ioloop模块式tornado的核心,他封装了操作管理epoll的工作
当ioloop实例启动的时候,ioloop将服务器启动用于监听的socket添加到epoll容器中,然后不断循环等待epoll返回
可以处理的socket(就是不断询问epoll)

当客户端发起连接后,ioloop拿到原先放在epoll中的服务端监听的socket,并且调用服务端处理socket的方法,接收连接请求,
并将新的监听socket放入epoll容器中,然后继续循环等待可处理的socket

当客户端发送请求数据后,ioloop从epooll中拿到接收数据的socket,并且调用服务端实例处理该socket的方法,
从socket中读取http报文数据,
解析后,调用application实例,进行路由分发,
实例化具体的requesthandler
执行其中具体的http方法
生成响应数据并且打包成http报文写入缓冲区

当与客户端的socket可写的时候,ioloop从epoll中拿到对应可写的socket,将缓存区中对应响应报文数据写入到socket中传回给客户端






















'''