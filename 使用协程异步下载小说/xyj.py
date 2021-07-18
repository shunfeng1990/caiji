"""
使用协程 异步 扒光一部西游记小说
https://dushu.baidu.com/pc/detail?gid=4306063500
"""

# 所有章节（名称，cid）
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}

# 章节的正文
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

"""
1. 同步操作：访问getCatalog 拿到所有章节的名称和cid
2. 异步操作：访问getChapterContent 下载所有章节内容
"""

import requests
import asyncio
import aiohttp
import aiofiles
import json

async def aiodownload(cid, book_id, title):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)  # 转换成json字符串
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open('novel/' + title, mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
                print(title, '下载完毕')

async def getCatalog(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    resp = requests.get(url, headers=headers)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # items就是对应每个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(aiodownload(cid, book_id, title))

    await asyncio.wait(tasks)
    print('全部下载完毕')



if __name__ == "__main__":
    book_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    asyncio.run(getCatalog(url))