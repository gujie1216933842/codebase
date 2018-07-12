import os

file_name = os.path.dirname(__file__) + '/new.txt'
fn = open(file_name, 'r')  #读写
fn1 = open(file_name, 'w')  #读写

lines = fn.readlines()
for line in lines:
    print(line)
    fn1.write(line.replace('大','小'))
fn.close()
