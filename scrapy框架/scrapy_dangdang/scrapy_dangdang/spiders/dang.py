import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    #如果是多页下载的话 那么必须调整的是allowed_domains的范围 一般情况下只写 域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = ' http://category.dangdang.com/pg'
    page = 1


    def parse(self, response):
        """ 
            pipelines   下载数据
            items       定义数据结构
        
            src = //div[@id="search_nature_rg"]/ul/li/a/img/@src
            name = //div[@id="search_nature_rg"]/ul/li/a/img/@alt
            price = //div[@id="search_nature_rg"]/ul/li/p[@class="price"]/span[1]/text()

            所有的selector的对象 都可以再次调用xpath方法
        
        """
        li_list = response.xpath('//div[@id="search_nature_rg"]/ul/li')

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            """ 
                第一张图片和其他图片的标签属性不一样
                第一张图片的src可以使用 其他的图片地址是data-originial 
            """
            if src:
                #如果图片有懒加载则直接使用data-original属性
                src = src
            else:
                #如果图片是第一张没有懒加载则使用src
                src = li.xpath('.//img/@src').extract_first()


            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()  
            #print(src,name,price)   

            book = ScrapyDangdangItem(src=src,name=name,price=price)

            #获取一个book 就将book交给pipelines            
            yield book
    
        #每一页的爬取的业务逻辑全都是一样的  所以我们只需要执行的那个页的请求再次调用parse方法就可以
        """  
            http://category.dangdang.com/cp01.01.02.00.00.00.html
            http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
            http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        """
        if self.page < 100:
            self.page = self.page+1
            
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
        
            print(url)

            #怎么去调用parse方法

            """ 
                scarpy.Request就是scrapy的get请求 
                url就是请求地址 callback是要执行的按个函数  不需要加() 
            """
            yield scrapy.Request(url=url,callback=self.parse)
