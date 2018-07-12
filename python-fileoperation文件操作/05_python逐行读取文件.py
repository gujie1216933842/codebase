import os

file_name = os.path.dirname(__file__) + '/new.txt'
new_file_name = os.path.dirname(__file__) + '/newfile.txt'
fn = open(file_name, 'r+')  #读写
fn1 = open(new_file_name, 'w')  #读写

lines = fn.readlines()
print(lines)
for line in lines:
    fn1.write(line.replace('大','小'))
fn.close()
