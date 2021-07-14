"""
 获取网易云音乐的评论，注意抓包post带参数请求 才能拿到结果
"""

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

# url是通过抓包找到的数据源地址，直接访问是空白，可能不是get请求，应该是post带参数请求
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 所以谷歌浏览器点击Headers 看下请求信息 是什么方式 带的什么参数，如果下拷贝出来参数
# 每次换个链接data参数都不同，所以想要彻底解决 就要还原出这个参数是怎么加密的，逆向处理一下。
data = {
    "params": "muyZnieTXY9YmfV3UniCEbrISazbiTz5PSF4C0zEUcKuZQdyOHZm8QycNk2/3rmg79L+ErBxbZWw87EBGqcp2XOnQIBNFqY0e87qXKjCBlGtMsrU9f9ui8ERXSHrVF49QDQPhzZOooQ8qgryC7YlKLx8DRCBH2ikUo3dBhXskFT2NXdIFwZlastLuX2Oe1msFv1R9vqHSaB6xLhk8hKBBEHNUl/gvUpMY2FVD/YJbMDTqHPxXQoIOoOlo8SiJQHlDc5aMtMiwt8FKyLL+TzkMniCTkAA1BVAiVNF38MHALY=",
    "encSecKey": "47b37ce5c17b6d6820503844476cd2968c482f035dd04566468976cb79904a19bd56964e625a6fa282b2884975726b9374367ba53f8862b46892e0b0073d30ea8215f0fa9a9a485e4dfd0e3ec928d23597c42b509535e790b43a93dba938e6776072c4a9107fe93dddeb3b36d875d855b707d5d851e4cb68213f84b34dafce47"
}
resp = requests.post(url, headers=headers, data=data)
hots = resp.json()['data']['comments']
for hot in hots:
    print(hot['content'])  # 拿到评论内容
