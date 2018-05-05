'''
用socket写一个ssh客户端
'''
import socket,os
'''
1.新建socket对象
2.绑定
2.1监听
3.等待接电话(保持电话通畅)
4.接受客户端返回的信息
5.返回客户端信息
'''

server = socket.socket()
server.bind(('localhost',9000))
server.listen()
conn,addr = server.accept()
while True:
    data = conn.recv(1024)

    print('客户端发来的信息:%s'%(data))

    cmd_res = os.popen(data).read()
    print('服务端返回给客户端的信息:%s'%(cmd_res))

    conn.send(cmd_res)

server.close()




