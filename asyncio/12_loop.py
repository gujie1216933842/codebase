import json, re, random, time
import pymysql.cursors
import asyncio, aiohttp

'''开始爬虫逻辑'''


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(url)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [main("http://47.97.165.75") for i in range(510)]  #windows上极限值大概510,超过了会报 too many file descriptors in select()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('comsume:{}'.format(time.time() - start_time))
