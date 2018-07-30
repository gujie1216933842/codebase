from concurrent.futures import as_completed, ThreadPoolExecutor
import time


def get_times(times):
    # time.sleep(times)
    print('get {} times'.format(times))
    return times


excutor = ThreadPoolExecutor(max_workers=2)
'''批量提交'''

urls = [2,3,4,6,8,5]
all_tasks = [excutor.submit(get_times, (url)) for url in urls]

'''as_complete是一个生成器'''
for future in as_completed(all_tasks):
    data = future.result()
    print('get {} page success'.format(data))
