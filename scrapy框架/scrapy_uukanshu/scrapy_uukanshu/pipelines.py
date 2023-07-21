# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class ScrapyUukanshuPipeline:
    

    def process_item(self, item, spider):
        
        #获得从item传递过来的数据
        novel_name = item['novel_name']
        chapter_name = item['chapter_name']
        content = item['novel_content']

        #小说路径
        novel_path = 'novel/' + str(novel_name)
        
        with open(str(chapter_name) + '.txt' ,'w',encoding='utf-8') as f:
            f.write(str(content))


        return item
"""         #判断文件夹是否创建
        if not os.path.exists(novel_path):
            #创建小说文件夹
            os.makedirs(novel_path)
        
        #判断章节是否爬取 如果没有爬取 则写入
        if not os.path.exists(novel_path + '/' + str(chapter_name)):
            #写入小说
            with open(novel_path + '/' + str(chapter_name),'w',enncoding='utf-8') as f:
                f.write(str(content)) """

        
