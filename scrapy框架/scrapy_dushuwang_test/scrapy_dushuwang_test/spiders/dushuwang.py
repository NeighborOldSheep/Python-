import scrapy


class DushuwangSpider(scrapy.Spider):
    name = "dushuwang"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["http://www.dushu.com/search.aspx?wd=%E7%9B%97%E5%A2%93%E7%AC%94%E8%AE%B0"]

    def parse(self, response):
        """  
            字符串
            content = response.text 

            二进制
            content = response.body
        """

        content = response.xpath('//div[@class="bookdetails-left"]//ul/li[1]//p')[0]
        print("=======================")
        print(content.extract())