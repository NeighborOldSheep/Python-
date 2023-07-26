import requests
from lxml import etree
import csv

# 存放链接的列表
new_links = []
number = 1
# 构造请求信息
for page in range(200):
    number = page * 15  # 计算每页的number值
    url = "https://www.chineseinla.com/f/page_viewforum/f_29/start_" + str(number) + ".html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    content = response.text

    # 构造xpath
    tree = etree.HTML(content)

    # 获取每个招聘信息的链接
    hire_links = tree.xpath('//div[@class="forum_line"]//div[@class="havenopage"]//a/@href')

    # 遍历发布链接拼接url
    for i in range(len(hire_links)):
        hire_links[i] = "https://www.chineseinla.com" + hire_links[i]
        new_links.append(hire_links[i])

print(len(new_links))

# 保存到csv
with open("hire_info.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(["招聘名称", "发布时间", "招聘信息"])

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
        print(hire_date)

        # 将每个招聘信息的各个元素连接为一个字符串，并写入CSV文件
        info_str = ",".join(hire_info)
        for title, date in zip(hire_title, hire_date):
            writer.writerow([title, date, info_str])
