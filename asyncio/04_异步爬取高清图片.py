import os
import aiohttp
import asyncio

# 图片的url数组
pic_list = ["http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_01origin_01_2017341744BB4.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_02origin_03_2017341744FC9.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_03origin_05_2017341744751.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_04origin_07_2017341744DD9.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_05origin_09_2017341744561.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_06origin_11_2017341744BE9.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_07origin_13_20173417443A2.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_5/gamersky_08origin_15_2017341744ABD.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_6/gamersky_02origin_03_2017341746E13.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_6/gamersky_03origin_05_201734174635D.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_6/gamersky_05origin_09_2017341746DF9.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_6/gamersky_06origin_11_20173417465EA.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_01origin_01_2017341747B6B.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_02origin_03_20173417474FD.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_03origin_05_20173417479AF.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_04origin_07_2017341747F66.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_05origin_09_20173417476EE.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_06origin_11_2017341747D76.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_07origin_13_20173417474FE.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_7/gamersky_08origin_15_2017341747B86.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_01origin_01_20173417485A9.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_02origin_03_2017341748B5D.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_03origin_05_20173417482D8.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_04origin_07_201734174812C.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_06origin_11_2017341748D6B.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_07origin_13_2017341748527.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_8/gamersky_08origin_15_2017341748C4C.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_01origin_01_2017341750ACF.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_02origin_03_2017341750ED1.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_04origin_07_2017341750B59.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_05origin_09_201734175013F.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_06origin_11_20173417507C7.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_9/gamersky_07origin_13_2017341750E4F.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_01origin_01_2017341753936.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_02origin_03_2017341753144.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_03origin_05_201734175369F.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_04origin_07_2017341753EFD.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_05origin_09_2017341753412.jpg",
            "http://img1.gamersky.com/image2017/03/20170304_zl_91_10/gamersky_06origin_11_201734175329A.jpg"]


# 将单个图片下载到本地
async def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as r:
            path = os.path.join('wallpapers', url.split('/')[-1])
            print(path)
            fp = open(path, 'wb')
            fp.write(await r.read())
            fp.close()


# def get_many(urls):
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [get_html(url) for url in pic_list]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


#get_many(pic_list)