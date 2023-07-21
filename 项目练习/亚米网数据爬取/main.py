import requests
from lxml import etree 
import pandas as pd
import matplotlib.pyplot as plt

""" 使用request + xpath爬取亚米网销量信息 """

def headers(pages):

    url = "https://www.yamibuy.com/zh/c/snack-beverage/1?page=" + str(pages)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }

    #定制请求信息
    response = requests.get(url=url,headers=headers)

    content = response.text

    return content 

def item_info(content):

    #构造xpath语句
    tree = etree.HTML(content)

    #获取物品  名称 价格 销量 
    item_name = tree.xpath('//div[@class="category-items"]//p[@class="item-title"]/a/text()')
    item_price = tree.xpath('//div[@class="category-items"]//div[@class="item-price__main"]//span[contains(@class,"price-normal")]/text()')
    item_sale = tree.xpath('//div[@class="category-items"]//div/p[@class="item__sale"]/text()')

    #将三个列表转换为相同的长度，并在无数据时用0填充
    max_len = max(len(item_name), len(item_price), len(item_sale))
    item_name += [''] * (max_len - len(item_name))
    item_price += [''] * (max_len - len(item_price))
    item_sale += ['0'] * (max_len - len(item_sale))

    item_sale = [sale.strip().replace(' ', '') for sale in item_sale]  # 清理空格
    item_price = [price.replace('$', '') for price in item_price]  # 清理美元符号

    #把商品数据保存为一个字典并返回
    item = pd.DataFrame({"Name" : item_name, "Price" : item_price, "Sale" : item_sale})

    return item

if __name__ == "__main__":
    pages = 63
    item_list = []
    for i in range(1,pages+1):
        content = headers(i)
        #通过循环不断的给item_list这个列表储存字典数据
        item = item_info(content)
        item_list.append(item)
    #合并所有dataFram
    total_item = pd.concat(item_list)
    #写入表格
    total_item.to_excel("data.xlsx",index=False)

    
