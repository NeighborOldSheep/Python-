from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://www.starbucks.com.cn/menu/'


response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content,'lxml')

#//ul[@class="grid padded-3 product"]//strong/text()

#使用bs4解析图片地址 和 名称
name_list = soup.select('.grid.padded-3.product strong')
src_list = soup.select('.grid.padded-3.product div')

#正则表达式来提取url里面的内容
pattenrs = r'url\("(.+)"\)'


#遍历星巴克产品名称
coffe_name_list = []
for name in name_list:
    coffe_name = name.get_text().replace("（热/冷）",'') .replace('/','')#.replace("热/冷",'')
    coffe_name_list.append(coffe_name)
    
#coffe_name_list.remove('摩卡（热/冷)')   
print(coffe_name_list)

#创建保存星巴克产品图片url的列表
coffe_img_list = []
for src in src_list:
    src = src.attrs.get('style')
    coffe_img = re.findall(pattenrs,src)
    #使用双层for循环拼接图片地址, 第一层for循环时提取url地址，第二层是因为每一个提取的url是单独的list遍历每个list并拼接
    for i in range(len(coffe_img)):
        url = 'https://www.starbucks.com.cn' + coffe_img[i]
        
        coffe_img_list.append(url)


#下载图片
for i in range(len(coffe_img_list)):
    urllib.request.urlretrieve( url = coffe_img_list[i], filename = 'img/' + str(coffe_name_list[i]) + '.jpg')


    
    


    
