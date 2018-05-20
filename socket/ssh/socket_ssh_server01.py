'''
用socket写一个ssh客户端
'''
import socket, os

'''
1.新建socket对象
2.绑定
2.1监听
3.等待接电话(保持电话通畅)
4.接受客户端返回的信息
5.返回客户端信息
'''

server = socket.socket()
server.bind(('0.0.0.0', 9000))
server.listen()
conn, addr = server.accept()
while True:
    data = conn.recv(1024)

    print('客户端发来的信息:%s' % (data))

    cmd_res = os.popen(data.decode()).read()
    if len(cmd_res) == 0:
        cmd_res = "ssh no output....."
    print('服务端返回给客户端的信息:%s' % (cmd_res))

    # 传递信息的长度
    cmd_res_size = len(cmd_res.encode("utf-8"))
    print("系统返回的数据长度:%s"%(cmd_res_size))
    #cmd_res = dict(content=cmd_res, content_size=cmd_res_size)
    conn.send(str(cmd_res_size).encode("utf-8"))
    conn.send(cmd_res.encode("utf-8"))

server.close()
