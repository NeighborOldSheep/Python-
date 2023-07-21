# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

#下载数据 管道
class ScrapyYamiPipeline:
    #打开文件
    def open_spider(self,spider):
        self.fp =  open('books.json','w',encoding='utf-8')

    #写入文件
    def process_item(self, item, spider):
        #注意这里item返回的是对象，而使用write的时候需要str类型 这里直接str()强制转换
        self.fp.write(str(item))

        return item
    
    #关闭文件
    def close_spider(self,spider):
        self.fp.close()


#下载图片 管道
class ImagePiepeline:

    def process_item(self,item,spider):

        #拼接图片地址
        url = 'https:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)

        return item