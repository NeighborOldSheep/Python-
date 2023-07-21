# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


# 如果想使用管道的话 那么就必须在settings中来开启管道
class ScrapyDangdangPipeline:

    # 在爬虫文件开始之前就执行的一个方法
    def open_spider(self,spider):
        #打开文件
        self.fp = open('book.json','w',encoding='utf-8')
    

    """  item就是 spider里面yield的对象book """
    def process_item(self, item, spider):
        #以下这种模式不推荐 因为每传递过来一个对象那么就打开一次文件 对文件操作过于频繁
        """  
            1. write()方法必须要写字符串，不能是其他的对象
            2. w模式 会每一个对象打开一次文件  然后覆盖之前的内容 然后关闭
           
             with open('book.json','a',encoding='utf-8') as f:
                f.write(str(item))

        """

        #写入文件
        self.fp.write(str(item))
        

        return item
    
    # 在爬虫文件只想完之后，执行的方法
    def close_spider(self,spider):
        #关闭文件
        self.fp.close()



""" 
    多条管道同时开启 
        1.定义管道类
        2.在settings中开启管道
        "scrapy_dangdang.pipelines.DangDangDownloadPipeline": 301,

"""
class DangDangDownloadPipeline:

    def process_item(self, item, spider):

        #下载图片
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)

        return item