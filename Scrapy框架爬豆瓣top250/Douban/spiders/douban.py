import scrapy
from Douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    offset = 0
    start_urls = [f'https://movie.douban.com/top250?start={str(offset)}&filter=']

    def parse(self, response):
        divs = response.xpath('//div[@class="item"]')
        for div in divs:
            item = DoubanItem()
            item['movie_name'] = div.xpath('./div[2]/div/a/span[1]/text()').extract_first()
            item['movie_director'] = div.xpath('./div[2]/div[2]/p/text()').extract_first().strip()
            item['movie_year'] = div.xpath('./div[2]/div[2]/p/text()[last()]').extract_first().strip()
            item['movie_rating'] = div.xpath('./div[2]/div[2]/div/span/text()').extract_first()
            yield item

        # if self.offset < 225:
        #     self.offset += 25
        #     url = f"https://movie.douban.com/top250?start={str(self.offset)}&filter="
        #     yield scrapy.Request(url, callback=self.parse)

        if len(response.xpath('//span[@class="next"]/a/@href')):
            url = response.xpath('//span[@class="next"]/a/@href').extract_first()
            yield scrapy.Request('https://movie.douban.com/top250' + url, callback=self.parse)
