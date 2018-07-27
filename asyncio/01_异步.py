import time, asyncio, random


async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist) - 1)
        print(alist.pop(c))
        await asyncio.sleep(1)


strlist = ["ss", "dd", "gg"]
intlist = [1, 2, 5, 6]
c1 = mygen(strlist)
c2 = mygen(intlist)
print(c1)  # <coroutine object mygen at 0x021C7F60>协程对象

# 要运行协程，要用事件循环
if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [c1, c2]
    loop.run_until_complete(asyncio.wait(tasks))
    print(' all finished ')
    end = time.time()
    print('comsume:{}'.format(end - start))
    loop.close()
