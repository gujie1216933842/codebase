'''
用户socket写一个ssh客户端
存在接收不全的问题
解决:
1.服务端先发大小给客户端
2.客户端先收大小
3.客户端再循环接收信息

'''

import socket

'''
步骤:
1.新建socket客户端
2.连接服务端
3.发送信息
4.接收服务端返回的信息
'''
client = socket.socket()
client.connect(('47.97.165.75', 9000))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_size = client.recv(1024)
    print("服务端返回的信息大小:%s"%(cmd_size))
    content = b''
    size = 0
    while size < int(cmd_size.decode()) :
        data = client.recv(1024)
        size += len(data)
        content +=data
    else:
        print(content.decode())
    print("客户端打印的的信息大小:%s" % (size))

client.close()
