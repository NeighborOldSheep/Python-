import requests 
from bs4 import BeautifulSoup
from lxml import etree

url = "https://www.jd.com/?country=USA"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

#像服务器发送请求
response = requests.get(url=url,headers=headers)
#获取网页源代码
content = response.text
print(content)
#构造xpath
tree = etree.HTML(content)

#获取图片路径
img_src_list = tree.xpath("//div[@class='slider']//img[@class='lazyimg_img']/@src")
#获取图片名称
img_name_list = tree.xpath("//div[@class='slider']//a[@class='slider_item seckill-item slider_active']/@title")

print(img_src_list)