# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyYamiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    """ 需要获取的数据 """
    src = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()