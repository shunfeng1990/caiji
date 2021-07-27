# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_director = scrapy.Field()
    movie_year = scrapy.Field()
    movie_rating = scrapy.Field()

