'''
多线程爬虫:在我们的程序中某些程序段并行的去执行
'''

import threading
import urllib.request
import re, time, os


class One(threading.Thread):
    def __init__(self, num, search):
        threading.Thread.__init__(self)
        self.num = num
        self.search = search

    def run(self):
        for i in range(self.num, 100, 2):
            snatch_pic(i, self.search)


class Two(threading.Thread):
    def __init__(self, num, search):
        threading.Thread.__init__(self)
        self.num = num
        self.search = search

    def run(self):
        for i in range(self.num, 100, 2):
            snatch_pic(i, self.search)


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


def snatch_pic(i, key):
    pic_dir = os.path.join(os.path.dirname(__file__), 'pic1/' + key)
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    pattern = '"pic_url":"//(.*?).jpg"'
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
                                     'pic1/' + key + '/page' + str(i) + 'few' + str(j) + '.jpg')
        print(pic_file_path)
        try:
            urllib.request.urlretrieve(pic_url, filename=pic_file_path)
        except Exception as e:
            print("异常:%s" % e)


key = "手机"
start_time = time.time()
a = One(0, key)  # 偶数
b = One(1, key)  # 奇数
a.start()
b.start()
end_time = time.time()
print("*****************************************************")
print("消耗时间%s" % (end_time - start_time))

