import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import xlwt
import re


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    savepath = '豆瓣Top250.xls'
    # 保存数据
    saveDate(datalist, savepath)


# 影片详情的链接对象
findLink = re.compile(r'<a class="" href="(.*?)">')
# 影片图片链接对象
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片名对象
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分对象
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # re.S 忽略换行符


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数 10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            data = []  # 保存一部电影的所有信息
            item = str(item)
            link = re.findall(findLink, item)[0]  # 影片详情链接
            data.append(link)

            imgsrc = re.findall(findImgSrc, item)[0]  # 影片图片链接
            data.append(imgsrc)

            titles = re.findall(findTitle, item)  # 影片名
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去除无关字符
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')  # 外国名留空

            rating = re.findall(findRating, item)[0]  # 影片评分
            data.append(rating)

            judge = re.findall(findJudge, item)[0]  # 评价人数
            data.append(judge)

            inq = re.findall(findInq, item)  # 概况
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]  # 影片相关内容
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 取掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉空格

            datalist.append(data)

    return datalist


# 得到指定一个url的内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveDate(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建Workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print('第{}条'.format(i))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])

    book.save(savepath)  # 保存


if __name__ == '__main__':
    main()
    print('爬取完毕...')
