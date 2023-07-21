import scrapy


class CorsaSpider(scrapy.Spider):
    name = "corsa"
    allowed_domains = ["www.corsaexoticsinc.com"]
    # 如果请求接口是html为结尾的 那么是不需要加/的
    start_urls = ["https://www.corsaexoticsinc.com/cars-for-sale?Make=BMW"]

    def parse(self, response):
        print('======================================')
