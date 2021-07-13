import requests

url = "https://www.pearvideo.com/video_1734967"  # 准备下载的视频链接
contId = url.split("_")[1]  # 拿到1734967 后续要用

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Referer": url  # 防盗链，溯源 从哪个页面来的
}

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"  # 抓包找到的数据源地址
resp = requests.get(videoStatusUrl, headers=headers)

dic = resp.json()
systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']  # JSON数据源里的视频地址 待处理的

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")  # 处理url把systemTime替换成contId
# print(srcUrl)  # 拿到了真是的视频地址

# 下载视频
with open(f"{contId}.mp4", mode='wb') as f:
    f.write(requests.get(srcUrl).content)
    print('ok')


