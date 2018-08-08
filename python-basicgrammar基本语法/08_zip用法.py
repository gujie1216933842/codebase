a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]

zipped = zip(a, b)
zipped1 = zip(a, c)

print(list(zipped))
# print(list(zipped1))
print(list(zip(*zipped)))
