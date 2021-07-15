"""
 xpath解析 简单爬取下ip138 看下自己的IP地址 是不是真正启用了代理模式
"""

import requests
from lxml import etree


proxies = {
    "https": "https://116.63.93.172:8081"  # 网站是http就写http
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
resp = requests.get("https://2021.ip138.com/", headers=headers, proxies=proxies)
resp.encoding = 'utf-8'

# 使用Xpath 解析下
html = etree.HTML(resp.text)
list_a = []
p = str(html.xpath('/html/body/p[1]/text()'))
a = html.xpath('/html/body/p[1]/a/text()')

true_ip = p.replace(r"['\n", '').replace(r"\n']", '').replace("[', ']", a[0])
print(true_ip)