"""
处理反爬 代理IP的使用
"""

import requests

# 49.75.59.242:3128  准备代理IP
proxies = {
    "https": "https://49.75.59.242:3128"  # 网站是http就写http
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
resp = requests.get("https://www.douban.com/", proxies=proxies, headers=headers)
resp.encoding = 'utf-8'
print(resp.text)
