
'''
python打印99乘法表

'''

for i in range(1, 10):
    for j in range(0, i):
        # print(i, j + 1)
        if i >= j + 1:
            if i == j + 1:
                end = '\n'
            else:
                end = ''
            print(str(i) + 'x' + str(j + 1) + '=' + str(i * (j + 1)) + '  ', end=end)
            j += 1

