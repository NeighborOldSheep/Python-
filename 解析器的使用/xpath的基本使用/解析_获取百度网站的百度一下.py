from lxml import etree 
import urllib.request

#(1)获取网页源码
#(2)解析    解析服务器响应的文件 etree.HTML

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

reqeust = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(reqeust)
content = response.read().decode('utf-8')

tree = etree.HTML(content)

#获取百度一下这四个字
keyword = tree.xpath('//input[@id="su"]/@value')

print(keyword)