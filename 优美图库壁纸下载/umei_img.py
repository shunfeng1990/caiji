# 爬取 下载图片 案例

import time
import requests
from bs4 import BeautifulSoup

def mian():
    get_data()

def get_data():
    url = 'https://www.umei.net/bizhitupian/diannaobizhi/'
    url2 = 'https://www.umei.net'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    # 用bs4 解析数据(把页面源代码交给BeautifulSoup处理)
    bs = BeautifulSoup(resp.text, "html.parser")

    lista = bs.find('div', class_='TypeList').find_all('a')
    total = 0  # 记录总数
    for a in lista:
        resp = requests.get(url2 + a.get('href'), headers=headers)  # 直接通过get就能拿到属性的值
        resp.encoding = 'utf-8'
        bs = BeautifulSoup(resp.text, "html.parser")
        div = bs.find('div', class_='ImageBody')  # 找到div
        img = div.find('img')  # 找到div里的img
        src = img.get('src')  # 通过get拿 src属性值
        # 下载图片
        resp2 = requests.get(src, headers=headers)
        img_name = src.split("/")[-1]  # 拿到src的最后一个/后面的数据
        with open('./img/' + img_name, 'wb') as f:
            f.write(resp2.content)
        print(img_name,'---- 下载成功')
        total += 1
        time.sleep(1)
    print('全部下载完毕! 共 {} 个'.format(total))


if __name__ == '__main__':
    mian()
