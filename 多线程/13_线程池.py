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
'''
urls = [3, 2, 4]
all_task = [excutor.submit(get_html, (url)) for url in urls]

for future in as_completed(all_task):
    data = future.result()
    print('get {} page'.format(data))
