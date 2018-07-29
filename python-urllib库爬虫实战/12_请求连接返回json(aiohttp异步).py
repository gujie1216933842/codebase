import urllib.request
import json, re, random
import pymysql.cursors
import asyncio, aiohttp

'''定义一个url链接池,存放待爬取的url'''
waitting_urls = []  # 等待爬取的urls
used_urls = set()  # 已经爬取过的urls


def get_urls():
    urls = []
    for i in range(1, 3227):  # 爬取的页码随时修改
        print(i)
        url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
            i, random.random())
        if url not in waitting_urls and url not in used_urls:
            waitting_urls.append(url)
            urls.append(url)
        return urls


'''开始爬虫逻辑'''


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [main(url) for url in waitting_urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


