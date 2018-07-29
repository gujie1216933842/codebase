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
    tasks = [main("http://47.97.165.75") for i in range(510)]
    '''
    windows上极限值大概510,超过了会报 too many file descriptors in select()
    因为asyncio内部用到了select，而select就是那个什么系统打开文件数是有限度的，
    上面的代码一次性将处理url的函数作为任务扔进了一个超大的List中，这就引起了错误，用这种形式无法写大规模爬虫
    
    这个报错的原因是因为 Python 调取的 select 对打开的文件字符有最大长度限制。  在此我们需要限制 并发数量。
     一次不要塞那么多任务，或者限制最大并发数量。这个仅供参考  。 数据少的时候正常  多了就不正常了。
     （建议还是使用限制loop的数量比较好）
    
    
    '''
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('comsume:{}'.format(time.time() - start_time))
