'''
epoll 为什么高效?
python的ioloop取询问epoll循环的时候,epoll每次返回的是真正可以处理的socket(真正可以干活的socket),
拿到有用的也是依次处理
这样,我不会把cpu时间不会浪费在无所事事的socket上了


tonardo工作原理:























'''