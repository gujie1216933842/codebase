import threading


def add(a, b):
    print(a + b)
    return a + b
def add1(a, b):
    print(a + b)
    return a + b



a = 1
b = 4
for i in range(10):
    print('--------------')
    add(a, b)
    t = threading.Thread(target=add1, args=(2, 4))
    t.start()
    print('--------------')
