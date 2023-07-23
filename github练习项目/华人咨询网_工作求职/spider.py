import requests
from lxml import etree
import csv


number = 0
#存放链接的列表
new_links = []

#构造请求信息
for page in range(1):
    url = "https://www.chineseinla.com/f/page_viewforum/f_29/famous/start_" + str(number) + ".html"
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
    response = requests.get(url=url, headers=headers)
    content = response.text 


    #构造xpath
    tree = etree.HTML(content)

    #https://www.chineseinla.com
    #获取每个招聘信息的链接
    hire_links = tree.xpath('//div[@class="forum_line"]//div[@class="havenopage"]//a/@href')


    #遍历发布链接拼接url
    for i in range(len(hire_links)):
        hire_links[i] = "https://www.chineseinla.com" + hire_links[i]
        new_links.append(hire_links[i])
    
    number += 15


    
   
# 保存所有招聘内容
information = []

# 遍历列表里的链接
for urls in range(len(new_links) - 1):
    response = requests.get(url=new_links[urls], headers=headers)
    content = response.text
    tree = etree.HTML(content)

    # 获取招聘名称
    hire_title = tree.xpath('//div[@class="post_title"]/span/h1/text()')
    # 获取发布时间
    hire_date = tree.xpath('//div[@class="post_time"]/span[1]/text()')
    # 获取招聘信息
    hire_info = tree.xpath('//div[@class="post_body"]/span/text()')

    # 每一个招聘帖子保存到一个列表
    hire_information = [hire_title, hire_date, hire_info]

    # 把每个帖子的列表保存进来
    information.append(hire_information)


     # 将每个招聘信息的各个元素打包成一行，并写入CSV文件
    for title, date, info in zip(hire_title, hire_date, hire_info):
        row = [title, date, info]
        information.append(row)

# 保存到csv
with open("hire_info.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(["招聘名称", "发布时间", "招聘信息"])
    # 写入招聘信息
    writer.writerows(information)


