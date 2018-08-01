from concurrent.futures import as_completed, ThreadPoolExecutor
import time, random, requests, json


def insert_mysql():
    pass

def get_data(url):
    res = requests.get(url)
    if res.status_code == 200:
        dict_data = json.loads(res.text)
        list_data = dict_data[0]['data']
        print(list_data)
        return res


if __name__ == "__main__":
    start_time = time.time()
    excutor = ThreadPoolExecutor(max_workers=10)
    all_tasks = [excutor.submit(get_data, (
            "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
        i, random.random()))) for i in range(1, 1000)]

    '''as_complete是一个生成器'''
    for future in as_completed(all_tasks):
        data = future.result()

    print('comsumer:{}'.format(time.time() - start_time))
