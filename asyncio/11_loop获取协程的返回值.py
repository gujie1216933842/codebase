import asyncio, time
from functools import partial

async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)  # 换成time.sleep(2) 整个程序就变成串型了
    return 'tom'


def callback(url,future):
    print(url)
    print('send email to tom')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html('http://www.baidu.com/'))
    task.add_done_callback(partial(callback,'http://www.baidu.com/'))
    loop.run_until_complete(task)
    print(task.result())
