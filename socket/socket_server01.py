#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-05-02 23:09:42
# @Last Modified by:   anchen
# @Last Modified time: 2018-05-02 23:37:23
'''
步骤:
1.绑定监听端口
2.监听
3.等电话打进来
4.电话来了
5.接收数据
'''
import socket

server = socket.socket()

server.bind(('localhost',6969)) #绑定要监听的端口

server.listen()  #监听

conn,addr = server.accept()  #等电话打进来
print(conn,addr)

print('电话来了!')
data = conn.recv(1024)

print('recv:',data)
conn.send(data.upper())

server.close()