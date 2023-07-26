import requests
from lxml import etree
import csv
import re

def process_url(url, xpath_expression):
    # 暂时存放的空列表
    url_links = []
    j = 0

    # 如果url是个列表把列表里的每个链接都进行访问
    if isinstance(url, list):
        # 创建一个辅助列表来存储新提取的链接
        new_links = []
        url_links = url[:5]
        for j in range(len(url_links)):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            }
            response = requests.get(url=url[j], headers=headers)
            response.encoding = "utf-8"
            content = response.text

            # 构造xpath语句
            tree = etree.HTML(content)

            index_url = tree.xpath(xpath_expression)
            
            #第一次访问返回值给province_url
            for i in range(len(index_url)):
                index_url[i] = "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/" + index_url[i]
                new_links.append(index_url[i])
                

        # 在每次调用完成后，将新链接赋值给url_links，覆盖之前的链接
        url_links = new_links

    # 如果url不是列表只进行一次访问
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        response.encoding = "utf-8"
        content = response.text

        # 构造xpath语句
        tree = etree.HTML(content)

        index_url = tree.xpath(xpath_expression)

        # 创建一个辅助列表来存储新提取的链接
        new_links = []
        for i in range(0, 10):
            index_url[i] = "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/" + index_url[i]
            new_links.append(index_url[i])

        # 在每次调用完成后，将新链接赋值给url_links，覆盖之前的链接
        url_links = new_links

    return url_links



province_url = process_url("http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/index.html",'//table[@class="provincetable"]//tr[@class="provincetr"]//a/@href') 

shi_url = process_url(province_url,'//table[@class="citytable"]//tr[@class="citytr"]/td[1]/a[1]/@href')
print(len(shi_url))
print(shi_url)

""" county_url = process_url(shi_url,'//table[@class="countytable"]//tr[@class="countytr"]/td[1]/a[1]/@href') """
county_links = []
for j in range(len(shi_url)):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url=shi_url[j], headers=headers)
    response.encoding = "utf-8"
    content = response.text

    # 构造xpath语句
    tree = etree.HTML(content)

    index_url = tree.xpath('//table[@class="countytable"]//tr[@class="countytr"]/td[1]/a[1]/@href')
    
    #第一次访问返回值给province_url
    for i in range(len(index_url)):
        index_url[i] = "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/11/" + index_url[i]
        county_links.append(index_url[i])

print(county_links)

town_url = []
for j in range(len(county_links)):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url=county_links[j], headers=headers)
    response.encoding = "utf-8"
    content = response.text

    # 构造xpath语句
    tree = etree.HTML(content)

    index_url = tree.xpath('//table[@class="towntable"]//tr[@class="towntr"]/td[1]/a[1]/@href')
    
    #第一次访问返回值给province_url
    for i in range(len(index_url)):
        index_url[i] = "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/11/01/" + index_url[i]
        town_url.append(index_url[i])
print(len(town_url))
print(town_url)


 # 获取社区居委会规划代码和名称
for k in range(len(town_url)):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url=town_url[k], headers=headers)
    response.encoding = "utf-8"
    content = response.text

    # 构造xpath语句
    tree = etree.HTML(content)

    # 获取名称和规划代码
    name_elements = tree.xpath('//table[@class="villagetable"]//tr[@class="villagetr"]/td[3]')
    code_elements = tree.xpath('//table[@class="villagetable"]//tr[@class="villagetr"]/td[1]')

    print(name_elements)
    print(code_elements)


        # 创建CSV文件并写入数据
    with open('国统计用区划代码和城乡划分代码.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Name', 'Code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for name_element, code_element in zip(name_elements, code_elements):
            name_text = name_element.text.strip() if name_element.text else ""
            code_text = code_element.text.strip() if code_element.text else ""
            writer.writerow({'Name': name_text, 'Code': code_text})
    