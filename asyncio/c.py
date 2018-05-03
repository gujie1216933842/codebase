'''
异步IO,asyncio执行的任务成为协程
'''

#非常正统的方式，运行的效果如下
import time
import requests
from concurrent.futures import ThreadPoolExecutor
 
NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'
 
def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']
     
# start = time.time()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
#         print('fetch({}) = {}'.format(num, result))
 
# print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))



#加入协程
import asyncio
'''
函数前添加 async 关键字 , 定义一个异步函数
'''
async def run_scraper_tasks(executor):
    loop = asyncio.get_event_loop()
 
    blocking_tasks = []
    for num in NUMBERS:
        task = loop.run_in_executor(executor, fetch, num)
        task.__num = num
        blocking_tasks.append(task)
 
    completed, pending = await asyncio.wait(blocking_tasks)
    results = {t.__num: t.result() for t in completed}
    for num, result in sorted(results.items(), key=lambda x: x[0]):
        print('fetch({}) = {}'.format(num, result))
 
start = time.time()
executor = ThreadPoolExecutor(3)
event_loop = asyncio.get_event_loop()
 
event_loop.run_until_complete(
run_scraper_tasks(executor)
)
 
print('Use asyncio+requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))



