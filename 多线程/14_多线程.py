from concurrent.futures import as_completed ,ThreadPoolExecutor
import time
def get_times(times):
    time.sleep(3)
    print('get {} times'.format(times))


urls = [2,3,4]
# all_task =
excutor = ThreadPoolExecutor(max_workers=2)
excutor.submit(get_times,(3))
excutor.submit(get_times,(2))

