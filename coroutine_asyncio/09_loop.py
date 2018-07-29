import asyncio,time

async  def  get_html(url):
    print('start get url')
    await asyncio.sleep(2)  #换成time.sleep(2) 整个程序就变成串型了
    print('end get url')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('http://www.baidu.com/{}'.format(i)) for i in range(20)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('time:{}'.format(start_time-time.time()))