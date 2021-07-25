import scrapy
import time
import math
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    time = str(int(time.time() * 1000))
    page = 1

    start_urls = [
        f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={time}&countryId=&cityId=&bgIds=&productId=& categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={page}&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        total_page = math.ceil(float(response.json()['Data']['Count']) / 10)  # 算出总页数
        job_list = response.json()['Data']['Posts']
        for job in job_list:
            item = TencentItem()
            item['name'] = job['RecruitPostName']
            item['job'] = job['Responsibility'].replace('\n', '').replace('\t', '').replace('\r', '')
            yield item

        if self.page < total_page:
            self.page += 1
            url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={time}&countryId=&cityId=&bgIds=&productId=& categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={self.page}&pageSize=10&language=zh-cn&area=cn'
            yield scrapy.Request(url, callback=self.parse)
