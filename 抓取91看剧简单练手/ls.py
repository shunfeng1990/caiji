"""
    抓取91看剧简单练手版
"""

# 视频地址
# https://91kanju.com/vod-play/54812-1-1.html

"""
流程：
    1. 拿到页面源码代码
    2. 从源代码提取m3u8的url地址
    3. 下载m3u8文件
    4. 读取m3u8文件，下载ts视频文件
    5. 合并ts视频
"""
import requests
import re


url = "https://91kanju.com/vod-play/54812-1-1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
# resp = requests.get(url, headers=headers)
#
# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)
#
# m3u8_url = obj.search(resp.text).group('url')
# # print(m3u8_url)
#
# resp2 = requests.get(m3u8_url, headers=headers)
# with open('file.m3u8', mode='wb') as f:
#     f.write(resp2.content)
#     print('m3u8 下载完毕')


# 解析m3u8文件
n = 1  # ts文件记录编号 不然视频错位乱了
with open('file.m3u8', mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()  # 删除左右两边的空格 换行符
        if line.startswith("#"):
            continue
        # 下载视频片段
        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode='wb')
        f.write(resp3.content)
        f.close()
        resp3.close()
        n += 1
    print('ts视频文件下载完毕')