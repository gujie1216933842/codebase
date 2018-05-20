import urllib.request
import re, os

'''
可以用urlretrieve()将把网页下载到本地作为静态网页
'''
urllib.request.urlretrieve("http://47.97.165.75/", filename=os.path.join(os.path.dirname(__file__), 'file/03.html'))
