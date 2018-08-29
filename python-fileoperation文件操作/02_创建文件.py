# coding=utf-8

import os

# aa = input()
# 文件名
file_name = os.path.dirname(__file__) + '/new.txt'
fn = open(file_name, 'r+')

# content = input()
for i in range(1000):
    fn.write(u'你大爷的\n')
fn.close()

