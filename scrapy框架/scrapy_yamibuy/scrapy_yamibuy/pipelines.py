# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import csv

class ScrapyYamibuyPipeline:

    def __init__(self):
        self.file = codecs.open('a.csv', 'w', encoding='utf_8_sig')


    def process_item(self, item, spider):
        fieldnames = ['src','name','sale','price']
        w = csv.DictWriter(self.file, fieldnames=fieldnames)
        w.writerow(item)
        return item