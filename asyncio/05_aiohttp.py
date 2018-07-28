'''
基于asyncio实现的
http协议
'''

'''爬取伯乐在线文章'''
'''asyncio爬虫,去重,入库'''

import asyncio
import re
from pyquery import PyQuery

import aiohttp
import aiomysql

stopping = False
start_url = "http://www.jobhole.com"
'''因为协程是单线程的,所以我们可以用列表来进行通信'''
waitting_urls = []  # 等待爬取的urls
seen_urls = set()  # 已经爬取过的urls


async def fetch(url, session):  # 定义了一个协程
    try:
        async  with session.get(url) as resp:  # get(url)是一个耗费网络io的过程
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)


'''定义一个在html页面汇总解析url的函数,因为解析是通过cpu来完成的,这里是不会耗费io的,所以我们直接定义一个函数'''


def extrack_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        # 判断url,踢出不符合条件的url
        if url and url.startswith('http') and url in waitting_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


'''定义一个协程'''


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    # 需要从html中解析出所有的url
    urls = extrack_urls(html)


'''定义一个协程,获取文章详情,并且解析入库'''


async def article_handler(url, session, pool):
    html = await fetch(url, session)
    seen_urls.add(url)  # 获取过的url添加进集合
    extrack_urls(html)  # 把url放入待爬取队列
    pq = PyQuery(html)
    title = pq('title').text()

    # 用aiomysql数据入库
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = " insert into testaiomysql (title)values ({})".format(title)
            await cur.excute(insert_sql)


'''定义一个消费者模型协程'''


async def consumer(pool):
    async with aiohttp.ClientSession as session:  # 建立连接
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print('start get url {}'.format(url))
            # 开始解析
            if re.match('http://jobbole.com/\d+/', url):
                if url not in seen_urls:
                    # 把创建的协程扔到时间循环中来
                    asyncio.ensure_future(article_handler(url, session, pool))

            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))


'''开始爬虫逻辑'''


async def main(loop):
    # 等待mysql连接池建立好
    pool = await aiomysql.create_pool(host='47.97.165.75', port=3306, user='root', password='123', db='test',
                                      loop=loop, charset='utf8', autocommit=True)

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extrack_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
