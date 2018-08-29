with open('withfile.txt','r+') as f:
    for line in f.readlines():
        print(line)
        newline = line.replace('with','关键字')
        f.write(newline)