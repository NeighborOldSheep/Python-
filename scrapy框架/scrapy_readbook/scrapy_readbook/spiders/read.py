import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook.items import ScrapyReadbookItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1179_1.html"]

    rules = (
        Rule(LinkExtractor(allow=r"/book/1179_\d+.html"), callback="parse_item", follow=False),
        )

    def parse_item(self, response):
        
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            book = ScrapyReadbookItem(name=name,src=src)
        
            #返回book对象每返回一个传递给管道一个
            yield book
