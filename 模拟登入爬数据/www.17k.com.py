import requests

url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

# 会话
session = requests.session()

# 1. 登入  如果抓不到登入的包 就点击选中一下 NetWork下面的 Preserve log
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "奔跑的骆驼63",
    "password": "qiujie5200"
}
resp = session.post(url, data=data)
# print(resp.text) 登入成功
# print(resp.cookies)  # 看cookie

# 2. 拿书架上的数据
# 刚才那个session中是有cookie的
resp2 = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp2.json())
json_data = resp2.json()
for item in json_data['data']:
    print(item['bookId'])  # 拿到书Id
    print(item['bookName'])  # 拿到书名
    print(item['authorPenName'])  # 拿到作者名

