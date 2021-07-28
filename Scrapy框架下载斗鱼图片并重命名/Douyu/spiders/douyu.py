import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseURL = "https://capi.douyucdn.cn/api/v1/getverticalroom?limit=20&offset="
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if not len(data_list):
            print('stop')
            return
        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['image_link'] = data['vertical_src']
            yield item

        self.offset += 20
        yield scrapy.Request(self.baseURL + str(self.offset), callback=self.parse)

