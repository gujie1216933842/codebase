import asyncio,time

async  def  get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html('http://www.baidu.com'))
    print('time:{}'.format(start_time-time.time()))