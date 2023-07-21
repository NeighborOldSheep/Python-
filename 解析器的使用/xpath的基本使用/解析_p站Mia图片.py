import urllib.request 
from lxml import etree


base_url = 'https://www.pornhub.com/album/72166651'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

#构造request请求
request_name = urllib.request.Request(url=base_url,headers=headers)

#获取网页源码
response_name = urllib.request.urlopen(request_name)
content_name = response_name.read().decode('utf-8')

#构造xpath解析
tree = etree.HTML(content_name)
#获取图片地址src
url_list = tree.xpath('//ul/li/div/a/@href')

#拼接每张图片src进入改网址
for i in range(len(url_list)):
    url = 'https://www.pornhub.com' + url_list[i]
    #print(url)
    #对于每个图片的网址构造request请求
    request = urllib.request.Request(url=url,headers=headers)
    #获取每个 图片页面的源码
    response= urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    #xpath tree构造
    tree = etree.HTML(content)
    #xpath 图片地址构造
    src_list = tree.xpath('//div[@id="photoImageSection"]//img/@src')
    #xpath 图片名称构造
    name_list = tree.xpath('//section[@id="photoInfoSection"]/h1/text()')
    
  
    #遍历列表下载图片
    for j in range(len(src_list)):
        img_url = src_list[j]
        #使用replace跟strip的时候replace在前面， 这里replace来替换掉双引号以防报错
        img_name = name_list[j].replace('"', '').strip()[:10]
        #print(img_name)
        urllib.request.urlretrieve(url=img_url,filename='pornhub_picture/' + img_name + '.png') 