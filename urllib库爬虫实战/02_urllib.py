import urllib.request
import re
for i in range(10000):
    url = "http://47.97.165.75:9000/search.html?aid=&aname=&sd=&ed="
    data = urllib.request.urlopen(url).read()
    data = data.decode("utf-8")
    pattern = '<span class="house-title">(.*?)</span>'
    mydata = re.compile(pattern).findall(data)
    print(mydata)