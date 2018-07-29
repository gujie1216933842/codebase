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
        print(html)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [main(
        "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
            i, random.random())) for i in range(200)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('comsume:{}'.format(time.time() - start_time))
