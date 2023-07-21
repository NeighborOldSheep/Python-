import scrapy
from scrapy_yami.items import ScrapyYamiItem

class YamiSpider(scrapy.Spider):
    name = "yami"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.09.01.00.00.00.html"]

    base_url = "http://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        #获取 书名 价钱  图片路径 的lixpath
        li_list = response.xpath('//ul[@id="component_59"]/li')
        
        #通过遍历获取每个书名 价格 图片的src data
        for i in li_list:
            #由于网站图片使用懒加载 除了第一个图片需要从data-orignal获取 判断是否是第一个图片
            if i.xpath('.//img/@src').extract_first() != 'images/model/guan/url_none.png' :
                src = i.xpath('.//img/@src').extract_first()
            else:
                src = i.xpath('.//img/@data-original').extract_first()

            name = i.xpath('.//img/@alt').extract_first()
            price = i.xpath('.//p[@class="price"]/span[@class="search_now_price"]').extract_first()

            #封装book对象给item
            book = ScrapyYamiItem(src=src,name=name,price=price)

            #每次传递一个book对象给管道
            yield book

            #构造100页的请求数据
            if self.page < 100:
                self.page = self.page + 1
                url = self.base_url + str(self.page) + '-cp01.09.01.00.00.00.html'

                #使用scrapy.Request去调用parse
                yield scrapy.Request(url=url,callback=self.parse)