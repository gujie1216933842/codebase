import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

# 进行索引也的抓取
base_url = "http://weixin.sogou.com/weixin?"

headers = {
    'Cookie': 'CXID=6C26CBB05726F4F7540F61AAC856BFCE; SUV=0012178472566EC75B1CE0CA49A14412; ad=kkllllllll2bGOqQlllllVHSiIylllllK91mElllll9lllllVVxlw@@@@@@@@@@@; SUID=5C6C56725C68860A5B091BD1000C4C51; IPLOC=CN3100; ABTEST=0|1532229455|v1; SNUID=5BC7291F636112E99B0CB624645BE58D; weixinIndexVisited=1; sct=1; JSESSIONID=aaabhZKExu97Egde9iHsw; ppinf=5|1532242234|1533451834|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQTElQkUlRTYlOUQlQjB8Y3J0OjEwOjE1MzIyNDIyMzR8cmVmbmljazoxODolRTklQTElQkUlRTYlOUQlQjB8dXNlcmlkOjQ0Om85dDJsdUFpVHhGMEc3bHJ6eDlub2NiWmpqVUlAd2VpeGluLnNvaHUuY29tfA; pprdig=bLA_T6e3sCzh2KqFU0Vf_wwnn-_hQW7QZtmSZgv1G9yC8X-EJsDpU-whGhuBkgQbcdNjmFQ8sdPcDUw6S-seSfDeJkVSSELYeccpRjlMDf_KEYluEC9zeskTTAT6_HfL5MMbjjI12O8cT0NTevL3mvQIRvJXBEz6rYyxWaR12wY; sgid=11-36170495-AVtUKTobyibcXqELUo5U2iahA; ppmdig=15322422350000009c853ac146623f857f1d6f2e20be1241',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

proxy_pool_url = "http://127.0.0.1:5000/get"

proxy = None

max_count = 10


def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    global proxy  # 作用:引用全局变量

    '''下面这段代码:注释的原因,因为代理池中的ip是一个公用ip,即同一时刻还在其他地方使用,所以不建议用max_count,否则一直会处在此时超限的判断中'''
    # if count >= max_count:
    #     print("Tried Too Many Counts")
    #     return None

    try:
        if proxy:
            proxies = {'http': 'http://' + proxy}
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        if response.status_code in [302, 301]:
            proxy = get_proxy()
            if proxy:
                print("Using Proxy", proxy)
                return get_html(url)
            else:
                print("Get Proxy Failed")
                return None
    except ConnectionError as e:
        print("Error Occur")
        count += 1
        return get_html(url, count)  # 如果失败,重新递归调用自己


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }

    queries = urlencode(data)
    url = base_url + queries

    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def main():
    for i in range(1, 101):
        print('循环次数:',i)
        html = get_index('风景', i)
        print(html)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                print(article_url)


if __name__ == "__main__":
    main()
