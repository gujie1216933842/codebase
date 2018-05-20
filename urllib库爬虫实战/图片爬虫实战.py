'''
抓取淘宝图片
https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&commend=all
&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0

https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&commend=all
&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44

https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&commend=all
&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88

https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&commend=all
&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1
&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132
'''
keyword = "女装"
url = "https://s.taobao.com/search?q=" + keyword + "&imgfile=&commend=all" \
                                                   "&ssid=s5-e&search_type=item" \
                                                   "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
                                                   "&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3" \
                                                   "&ntoffset=3&p4ppushleft=1%2C48&s=44"
import urllib.request

html = urllib.request.urlopen(url).read()
for i in range(100):
    print(i)
