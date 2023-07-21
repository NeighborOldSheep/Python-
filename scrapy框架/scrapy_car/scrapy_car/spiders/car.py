import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # 如果你的请求的接口是  html为结尾的 那么是不需要加 / 的
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        content = response.text
        print('=============================')
        #name_list = response.xpath('//div[@id="dealerTab"]//a[@class="show-name"]/text()')
        name_list = response.xpath('//div[@class="list-cont"]//a[@class="font-bold"]/text()')
        price_list = response.xpath('//div[@class="list-cont"]//span[@class="font-arial"]/text()')
      
        for i in range(len(name_list)):
            print(name_list[i].extract(),price_list[i].extract())