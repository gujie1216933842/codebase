import requests, random, time

start_time = time.time()
for i in range(1,101):
    url = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1801_cxda&TABKEY=tab1&PAGENO=%s&random=%s" % (
        i, random.random())

    data = requests.get(url)
    print(data.text)

print(time.time() - start_time)
