'''
代理服务器:是一个处于我们与互联网中间的服务器,如果使用代理服务器,我们浏览信息的时候,先向代理服务器发出请求,
          然后又代理服务器向互联网获取信息,再返给我们

爬虫使用代理服务器的原因:如果我们用自己的ip去爬取,时间久了,会被封掉

                    西刺代理ip

'''
import urllib.request


def use_proxy(url, proxy_addr):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    # 创建opener对象
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    # 载入opener
    urllib.request.install_opener(opener)
    # 开始爬取
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    return data
url = "http://47.97.165.75"
proxy_addr = "27.152.115.235:8118"
data = use_proxy(url,proxy_addr)
print(data)