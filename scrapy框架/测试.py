import requests 
from lxml import etree 

url = 'https://www.yamibuy.com/zh/c/snack-beverage/1?'

headers = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get(url=url,headers=headers)

content = response.text

tree = etree.HTML(content)

#产品名称xpath路径
item_list = tree.xpath('//div[@class="category-items"]//a/img/@alt')
#产品图片地址xpath路径  由于有懒加载需要判断是@src 还是@data-src
item_pic = tree.xpath('//div[@class="category-items"]//a/img/@data-src')
#产品销量(需要清洗空格)
item_sale = tree.xpath('//div[@class="category-items"]//p[@class="item__sale"]/text()') 
#产品价格
item_price = tree.xpath('//div[@class="category-items"]//div[@class="item-price"]//span[@class="price-normal price-valid word-bold-price"]/text()')

print(content,item_price,item_pic,item_sale,item_list)