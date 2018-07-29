import time, asyncio, random

def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        time.sleep(1)




# 要运行协程，要用事件循环
if __name__ == '__main__':
    start = time.time()
    strlist = ["ss", "dd", "gg"]
    intlist = [1, 2, 5, 6]
    c1 = mygen(strlist)
    c2 = mygen(intlist)
    print(' all finished ')
    end = time.time()
    print('comsume:{}'.format(end - start))
