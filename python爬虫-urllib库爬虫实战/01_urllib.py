import urllib.request
import re

url = "http://47.97.165.75"
data = urllib.request.urlopen(url).read()
print(data)
