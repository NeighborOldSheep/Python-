import scrapy
import re
from scrapy_uukanshu.items import ScrapyUukanshuItem

def clean_filename(filename):
    # 将非法字符替换为下划线
    cleaned_filename = re.sub(r'[^\w\-_. ]', '_', filename)
    # 删除多余的空格和下划线
    cleaned_filename = re.sub(r'[_\s]+', '_', cleaned_filename).strip('_')
    return cleaned_filename

class NovelSpider(scrapy.Spider):
    name = "novel"
    allowed_domains = ["www.uukanshu.com"]
    start_urls = ["https://www.uukanshu.com/list/yanqing-1.html"]

    

    def parse(self, response):
        """ 获取玄幻类小说的所有小说url和名称的路径"""
        book_list = response.xpath('//div[@class="content clearfix"]/span[@class="list-item"]')
    
       
        for i in book_list:
            #遍历url拼接
            url = 'https://www.uukanshu.com' + str(i.xpath('./a[@class="bookImg"]/@href').extract_first())
            #获取每个小说的名称
            book_name = i.xpath('.//a[@class="bookImg"]/@title').extract_first()
            print(url)
            #这里的callback  = self.parse_detail 是来处理每个小说url里面的内容
            request = scrapy.Request(url=url,callback=self.parse_detail)

            #将书名传递给下一个解析函数 使用request meta字典
            request.meta["book_name"] = book_name

            #每次返回一个url给 parse_detail来处理
            yield request
    
    def parse_detail(self,response):
        #获取每个小说章节url
        chapter_list = response.xpath('//ul[@id="chapterList"]/li')

        for chapter in chapter_list:
            #拼接每个章节url
            chapter_url = chapter.xpath('./a/@href').extract_first()
            chapter_url = 'https://www.uukanshu.com' + str(chapter_url)
            #获取每个章节名称
            chapter_name = chapter.xpath('./a/@title').extract_first()
            chapter_name = clean_filename(chapter_name)

            #接受prase函数里面的book_name变量
            novel_name = response.meta['book_name']


            #使用scrapy.Request传递给prase_content函数
            request = scrapy.Request(url=chapter_url,callback=self.parse_content,meta={'chapter_name':chapter_name,'novel_name':novel_name})

            yield request

    def parse_content(self,response):
        """ 
        获取小说内容
            通过分析发现 有些小说使用p标签有些使用br分隔所以使用if语句判断

            注意: 我们提取数据是这里已使用extract()因为我们需要把每个章节的内容以列表返回
                    通过join方法来拼接字符串 和清洗数据  如果使用extract_first() 拼接很麻烦
        """

        if response.xpath('//div[@class="contentbox"]//p/text()'):
            #使用p标签的内容
            chapter_content = response.xpath('//div[@class="contentbox"]//p/text()').extract()
        else:
            #使用p标签以外的手段
            chapter_content = response.xpath('//div[@id="contentbox"]/text()').extract()
        
        #清洗数据
        chapter_content = '\n'.join(chapter_content)

        #接受小说名称和章节名称
        novel_name = response.meta['novel_name']
        chapter_name = response.meta['chapter_name']

        print(chapter_content)

        #封装item对象
        novel = ScrapyUukanshuItem(novel_name = novel_name, chapter_name = chapter_name, novel_content = chapter_content)

        #把novel对象传递给管道进行下载
        yield novel
        

