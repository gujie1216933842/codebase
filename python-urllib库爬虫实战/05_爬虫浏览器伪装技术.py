'''爬虫浏览器伪装技术'''

import urllib.request

'''如果正常爬取,会返回403 forbidden错误'''

url = "https://www.whatismyip.com/"
file = b''
try:
    file = urllib.request.urlopen(url).read()
except Exception as e:
    print("异常:%s" % e)
print(file)
# exit()


'''添加headers参数'''
url = "https://www.whatismyip.com/"
headers = ("user-agent",
           "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36")
opener = urllib.request.build_opener()
'''urlopen()方法不支持有header报文的请求,所以这里我们用build_opener()方法'''
opener.addheaders = [headers]
file = opener.open(url).read()
print(file)
