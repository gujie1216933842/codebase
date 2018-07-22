import requests
from urllib.parse import urlencode

# 进行索引也的抓取
base_url = "http://weixin.sogou.com/weixin?"

headers = {
    'Cookie': 'CXID=6C26CBB05726F4F7540F61AAC856BFCE; SUV=0012178472566EC75B1CE0CA49A14412; ad=kkllllllll2bGOqQlllllVHSiIylllllK91mElllll9lllllVVxlw@@@@@@@@@@@; SUID=5C6C56725C68860A5B091BD1000C4C51; IPLOC=CN3100; ABTEST=0|1532229455|v1; SNUID=5BC7291F636112E99B0CB624645BE58D; weixinIndexVisited=1; sct=1; JSESSIONID=aaabhZKExu97Egde9iHsw; ppinf=5|1532242234|1533451834|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQTElQkUlRTYlOUQlQjB8Y3J0OjEwOjE1MzIyNDIyMzR8cmVmbmljazoxODolRTklQTElQkUlRTYlOUQlQjB8dXNlcmlkOjQ0Om85dDJsdUFpVHhGMEc3bHJ6eDlub2NiWmpqVUlAd2VpeGluLnNvaHUuY29tfA; pprdig=bLA_T6e3sCzh2KqFU0Vf_wwnn-_hQW7QZtmSZgv1G9yC8X-EJsDpU-whGhuBkgQbcdNjmFQ8sdPcDUw6S-seSfDeJkVSSELYeccpRjlMDf_KEYluEC9zeskTTAT6_HfL5MMbjjI12O8cT0NTevL3mvQIRvJXBEz6rYyxWaR12wY; sgid=11-36170495-AVtUKTobyibcXqELUo5U2iahA; ppmdig=15322422350000009c853ac146623f857f1d6f2e20be1241',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            pass
    except ConnectionError as e:
        return get_html(url)  # 如果失败,重新递归调用自己


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }

    queries = urlencode(data)
    url = base_url + queries
    print(url)

    html = get_html(url)
    # print(html)


def main():
    for i in range(1000):
        print(i)
        get_index('风景', i)


if __name__ == "__main__":
    # get_index('风景', 1)
    main()
