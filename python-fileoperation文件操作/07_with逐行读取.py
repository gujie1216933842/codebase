newline = ''
with open('withfile.txt','r+') as f:
    for line in f.readlines():
        print(line)
        newline += line.replace('关键字','你好')

with open('withfile.txt','w') as f:
    f.write(newline)
