import scrapy
from scrapy_yamibuy.items import ScrapyYamibuyItem

class SnackSpider(scrapy.Spider):
    name = "snack"
    allowed_domains = ["www.yamibuy.com"]
    start_urls = ["https://www.yamibuy.com/zh/c/snack-beverage/1?page=1"]

    base_url = 'https://www.yamibuy.com/zh/c/snack-beverage/1?'
    page = 1

    def parse(self, response):
        #食品 名称 图片 价格 销量的xpath路径  
        """ 
            大坑注意: 
                由于该网站不能使用item-card来匹配到每个信息的div但是前端代码中商品只有48个但是该标签
                    有50个所以我们要用position <= 48 来获取前48个div元素 排除掉后面两个空标签
        """
        snack_list = response.xpath('//div[@class="category-items"]/div[position() <= 48]')

        #遍历 并重新调用xpath方法
        for snack in snack_list:
            #extract_first() 提取列表第一个元素
            
            #判断图片是否有懒加载
            if snack.xpath('.//a/img/@data-src'):
                #图片有懒加载:
                snack_src = snack.xpath('.//a/img/@data-src').extract_first()
            else:
                #图片是前几长没有懒加载
                snack_src = snack.xpath('.//a/img/@src').extract_first()

            snack_name = snack.xpath('.//a/img/@alt').extract_first()
            
            """ 由于该网站价格css匹配比较特殊这里使用 xpath的contains方法"""
            snack_price = snack.xpath('./div[@class="item-price"]/div[@class="item-price__main"]/span[contains(@class,"word-bold-price")]/text()').extract_first().strip()
         
            snack_sale = snack.xpath('./div//p[contains(@class,"item__sale")]/text()').extract_first().strip()
            
            #封装食品对象
            snack_item = ScrapyYamibuyItem(src=snack_src, name=snack_name, sale=snack_sale,
                                           price=snack_price)

            #把snack_item传递给管道进行下载
            yield snack_item
            

            #一共63页
            if self.page < 63:
                self.page = self.page + 1
                url = self.base_url + "page=" + str(self.page)

                #递归传递每页的数据给parse()函数来解析每个页面的内容
                yield scrapy.Request(url=url,callback=self.parse)

            