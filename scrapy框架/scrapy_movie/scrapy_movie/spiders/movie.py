import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dydytt.net"]
    start_urls = ["http://www.dydytt.net/html/gndy/dyzz/index.html"]

    base_url = 'http://www.dydytt.net/html/gndy/dyzz/'
    page = 2

    def parse(self, response):
        #要第一页的名字 和 第二页的图片
        
        a_list = response.xpath('//div[@class="co_content8"]//a[@class="ulink"]')

        for a in a_list:
            #获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            
            #第二页的地址是
            url = "https://www.dydytt.net" + href

            #对第二页的链接发起访问
            """ 这里的meta是字典类型,可以把这个函数的变量传递到callback这个函数 """
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})
            

        if self.page < 100:
            #如果不到100页每次加一
            self.page = self.page + 1
            next_page = self.base_url + 'list_23_' + str(self.page) + '.html'
            
            #递归parse函数遍历1-100页的数据
            yield scrapy.Request(url=next_page,callback=self.parse)

            
            
    
    def parse_second(self,response):
        #注意 如果拿不到数据的情况下 一定要检查xpath语法 是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        
        #接受meta传递的name变量
        name = response.meta['name']

        movie = ScrapyMovieItem(src=src,name=name)

        #传递movie给管道
        yield movie

