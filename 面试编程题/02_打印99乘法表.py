list_hang = []
for i in range(1, 10):
    for j in range(0, i):
        # print(i, j + 1)
        if i >= j + 1:
            print(str(i) + 'x' + str(j + 1) + '=' + str(i * (j + 1)))
            j += 1


'''
1
0
1x1 = 1
2x1 = 2   2x2 = 4

3x1 = 3
            
            
            # '''
#
# for i in range(1, 1):
#     print(i)
