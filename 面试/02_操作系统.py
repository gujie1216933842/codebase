'''
1.select poll 和epoll
  三个都有io多路复用的机制
  io多路复用就是通过一种机制,一个进程可以监视多个描述符,一旦一个描述符就绪,就能够通知程序进行读写操作
  但是select poll 和epoll本质上都是同步io,也就是说读写过程是阻塞的,而异步io不需要自己读写,异步io的实现

  epoll并不一定比select好
  在高并发的情况下,连接活跃度不是很高,epoll比select好,web高并发网站
  在并发性不高,同时连接很活跃,select比epoll好,游戏开发




'''