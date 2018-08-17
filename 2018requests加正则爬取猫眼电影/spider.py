import requests
import re, json, platform
from requests.exceptions import RequestException
from multiprocessing import Pool


def get_proxy_url():
    op = platform.platform()
    if 'Linux' in op:
         proxy_pool_url = 'http://47.97.165.75:5000/get'
    else:
        proxy_pool_url = 'http://127.0.0.1:5000/get'

    return proxy_pool_url


def get_proxy():
    try:
        proxy_url = get_proxy_url()
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except ConnectionError:
        return None


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        proxies = {'http': 'http://' + get_proxy()}
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException as e:
        # print('异常:'.format(e))
        return None


def parse_one_page(html):
    # pattern = re.compile(
    #     '<dd>.*?board-index.*?(\d+)</i>.*?title="(.*?)".*?class="poster-default">src="(.*?)">.*?class="star">(.*?)'
    #     '</p>上映时间：(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i></p>', re.S)
    # pattern = re.compile(
    #     '<dd>.*?title="(.*?)" class="image-link" data-act="boarditem-click" data-val="{movieId:837}"><img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" /><img data-src="(.*?)" alt="唐伯虎点秋香" class="board-img" /></a><div class="board-item-main"><div class="board-item-content"><div class="movie-item-info"><p class="name"><a href="/films/837" title="唐伯虎点秋香" data-act="boarditem-click" data-val="{movieId:837}">唐伯虎点秋香</a></p><p class="star">主演：(.*?)</p><p class="releasetime">(.*?)</p>    </div><div class="movie-item-number score-num"><p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p></div></div></div></dd>',re.S)

    pattern = re.compile(
        '<dd>.*?title="(.*?)".*?data-src="(.*?)"', re.S)

    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'title': item[0],
            'img_url': item[1]
        }


def write_to_file(content):
    with open('maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset={}'.format(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    # for i in range(10):
    #     main(i * 10)
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
