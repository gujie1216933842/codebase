from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed

import time


def get_html(times):
    time.sleep(times)
    print("get times {} success".format(times))
    return times


excutor = ThreadPoolExecutor(max_workers=2)
'''
批量task
一旦子线程执行完成,主线程中的as_complete能收到
map方法实现
'''
urls = [3, 2, 4]

for data in excutor.map(get_html, urls):
    print('get {} page'.format(data))
