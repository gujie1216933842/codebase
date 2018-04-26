
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-04-25 22:30:06
# @Last Modified by:   anchen
# @Last Modified time: 2018-04-25 23:39:14



'''
二分查找法
'''
def binarySearch(l, t):
    low, high = 0, len(l) - 1
    while low < high:           
        mid = int((low + high) / 2)
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if l[low] == t else False
 
if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    # print (binarySearch(l, 12) )
    # print (binarySearch(l, 1) )
    # print (binarySearch(l, 13) )
    # print (binarySearch(l, 444) )
l = [1, 4, 12, 45, 66, 99, 120, 444]
# print(binarySearch(l, 12) )





class A(object):
    """docstring for ClassName"""
    # name = ""
    # age = 0
    # job = "doctor"
    def setName(self):
        #self.name = "xiaoming"
        #print(self.name)
        print('hahahaha')

    @classmethod 
    def setAge(cls):
        #cls.age = 28 
        cls().setName()   #此处如果 cls.setName()就会报错

    @staticmethod
    def jobs():
        A().setName()
        print('staticmethod')   #此处如果 A.setName()就会报错

# A.jobs()
# A.setAge()

'''
线程
'''

import threading
import time
 
def worker(num):
    """
    thread worker function
    :return:
    """
    # time.sleep(3)
    #print("Thread %d" % num)
    return
 
for i in range(200):
    t = threading.Thread(target=worker,args=(i,),name="t.%d" % i)
    t.start()
    #print(t.getName())



'''
异步IO,asyncio执行的任务成为协程
'''

#非常正统的方式，运行的效果如下
import time
import requests
from concurrent.futures import ThreadPoolExecutor
 
NUMBERS = range(12)
# URL = 'http://httpbin.org/get?a={}'
 
# def fetch(a):
#     r = requests.get(URL.format(a))
#     return r.json()['args']['a']
     
# start = time.time()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
#         print('fetch({}) = {}'.format(num, result))
 
# print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))



#加入协程
import asyncio
 
async def run_scraper_tasks(executor):
    loop = asyncio.get_event_loop()
 
    blocking_tasks = []
    for num in NUMBERS:
        task = loop.run_in_executor(executor, fetch, num)
        task.__num = num
        blocking_tasks.append(task)
 
    completed, pending = await ,asyncio.wait(blocking_tasks)
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






        












