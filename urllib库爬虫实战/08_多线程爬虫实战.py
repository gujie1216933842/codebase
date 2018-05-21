'''
多线程爬虫:在我们的程序中某些程序段并行的去执行
'''

import threading
import urllib.request
import re, time, os

class One(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        if self.num%2==0:
            for i in range(10):
                print("我是线程A")
        else:
            for i in range(10):
                print("我是线程A")




a = One(0)  #偶数
b = One(1)  #奇数
a.start()
b.start()

def func(keyword, i, pattern):
    keyword = urllib.request.quote(keyword)  # 用来处理请求字符串中中文
    url = "https://s.taobao.com/search?q=" + keyword + "&imgfile=&commend=all" \
                                                       "&ssid=s5-e&search_type=item" \
                                                       "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
                                                       "&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3" \
                                                       "&ntoffset=3&p4ppushleft=1%2C48&s=" + str(i * 44)
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        html = ''
        print('爬取网页异常:%s' % e)

    ret = re.compile(pattern).findall(html)
    return ret


# 当前日期
# now_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def snatch_pic(key):
    pic_dir = os.path.join(os.path.dirname(__file__), 'pic/' + key)
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    pattern = '"pic_url":"//(.*?).jpg"'
    for i in range(100):
        ret = func(key, i, pattern)
        # 当天的日期
        data = time.time
        for j in range(0, len(ret)):
            # 这里用urlretrieve爬取图片
            # 图片链接
            pic_url = "http://" + ret[j] + ".jpg"
            print(pic_url)
            # 要保存的图片路径
            pic_file_path = os.path.join(os.path.dirname(__file__),
                                         'pic/' + key + '/page' + str(i) + 'few' + str(j) + '.jpg')
            print(pic_file_path)
            try:
                urllib.request.urlretrieve(pic_url, filename=pic_file_path)
            except Exception as e:
                print("异常:%s" % e)


key = "男装"
snatch_pic(key)

