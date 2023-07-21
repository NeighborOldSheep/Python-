# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyUukanshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #小说名称
    novel_name = scrapy.Field()
    #章节名称
    chapter_name = scrapy.Field()
    #章节内容
    novel_content = scrapy.Field()
