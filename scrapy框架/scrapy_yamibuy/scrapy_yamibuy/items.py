# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyYamibuyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #需要的数据
    src = scrapy.Field()    #食品图片地址  
    name = scrapy.Field()   #食品名称
    sale = scrapy.Field()   #食品销量
    price = scrapy.Field()  #食品价格
