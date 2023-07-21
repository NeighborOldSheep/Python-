import requests 
from bs4 import BeautifulSoup
from lxml import etree
import os
import re 
import time

def clean_filename(filename):
    # 将非法字符替换为下划线
    cleaned_filename = re.sub(r'[^\w\-_. ]', '_', filename)
    # 删除多余的空格和下划线
    cleaned_filename = re.sub(r'[_\s]+', '_', cleaned_filename).strip('_')
    return cleaned_filename


#小说网址
url = "https://www.uukanshu.com/b/29676/"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie': 'fcip=111; _ga=GA1.2.239028119.1678417939; _gid=GA1.2.1065899300.1678417939; __gads=ID=c1b49c01c767ad6a-229b8ed9bbdb008d:T=1678417939:RT=1678417939:S=ALNI_MY8jUR0NNXLMjFThr6hOdifuzwmXg; __gpi=UID=0000095a177cbfc3:T=1678417939:RT=1678417939:S=ALNI_MYLjp6W1t8y0rvyt9yK-Kt-ke6Egg; lastread=29676%3D181199%3D%u7B2C%u4E8C%u5343%u516B%u767E%u4E03%u5341%u56DB%u7AE0%20%u9F99%u5899%u5B88%u536B; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2C%5B%5B1678421722%2C72000000%5D%2C%221YNN%22%5D%2Cnull%2C%5B%5D%5D; FCNEC=%5B%5B%22AKsRol_UizCrxWis3Uutw-e5bMHiBHJXsrnb84Pt4_uk7qG4oM5gy4Uk1XokWvPVnfM5e4bcOVdKTbPeDJM0EqbLpTIuDb8SZiDsaIluv4MzmRuQjvROfottA7l5JqrWTJV0tlvIFo1RlKbOnlduzA38jFDX_3iwiA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; ASP.NET_SessionId=dyzib5qmsxiyjwn12aegfyh3; __atuvc=17%7C10; __atuvs=640acb7e0aa22eba000; __atssc=google%3B1; _gat=1',
}

#代理池ip地址
proxy = {
    'http' : '121.13.252.62:41564',
    'http' : '27.42.168.46:55481',
    'http' : '112.14.47.6:52024',
    'http' : '121.13.252.58:41564',
    'http' : '222.74.73.202:42055',
    'http' : '61.216.156.222:60808',
    'http' : '117.114.149.66:55443',

}


#模拟浏览器发送请求
response = requests.get(url=url,headers=headers,proxies=proxy)
#返回网页源码
content = response.text 

#构造xpath
tree = etree.HTML(content)

#获取书名
novel_title = tree.xpath("//dd[@class='jieshao_content']/h1/a/@title")

#获取每个章节的地址
a_list = tree.xpath("//ul[@id='chapterList']//a/@href")

#获取每个章节的名称
name_list = tree.xpath("//ul[@id='chapterList']//a/text()")
#print(type(a_list))

#遍历每个章节地址
url_list = []
for i in range(len(a_list)):
    url = "https://www.uukanshu.com" + str(a_list[i]) 
    url_list.append(url)
print(url_list)

#创建此小说的文件夹 以小说名命名
path = "novel/"
new_folder = novel_title[0]


#遍历所有章节并且全部下载
for j in range(len(a_list)):
    #访问每个章节生成浏览器请求
    chapter_response = requests.get(url_list[j],headers=headers,proxies=proxy)
    #返回章节源码
    chapter_content = chapter_response.text 

    #构造xpath函数
    chapter_tree = etree.HTML(chapter_content)
    
    #由于有些章节会使用 p标签而有些章节则不用我们需要进行判断
    if chapter_tree.xpath('//div[@class="contentbox"]//p/text()'):
        #获取每个章节的内容
        novel_content_list = chapter_tree.xpath('//div[@class="contentbox"]//p/text()')
    else:
        #没有p标签的情况
        novel_content_list = chapter_tree.xpath('//div[@id="contentbox"]/text()')
        
    

    novel_content = '\n'.join(novel_content_list).strip()   #这里\n是保存的时候方便阅读

    chapter_name = clean_filename(name_list[j])
    #print(chapter_name)



    #检查文件夹是否存在  如果存在直接下载小说
    if not os.path.exists(os.path.join(path,new_folder)):
        #如果不存在则创建并下载小说;
        os.makedirs(os.path.join(path,new_folder))
        #下载小说
        with open('novel/' + new_folder + '/'+ str(j) + chapter_name  +'.txt','w',encoding='utf-8') as f:
            f.write(novel_content)
        print(name_list[j] + "下载完成")
    
    #文件夹存在直接下载
    else:
        #下载小说
        with open('novel/' + new_folder + "/" + str(j) + chapter_name +  '.txt','w',encoding='utf-8') as f:
            f.write(novel_content)
        print(name_list[j] + "下载完成")

    time.sleep(1)


print(novel_title[0] + "已经下载完成")


