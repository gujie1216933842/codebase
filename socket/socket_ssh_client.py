'''
用户socket写一个ssh客户端
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
client.connect(('localhost', 9000))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode())
    cmd_res = client.recv(1024)
    print('客户端接收服务端返回的信息:%s' % (cmd_res.decode()))


client.close()
