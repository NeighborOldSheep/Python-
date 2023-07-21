import requests 
from lxml import etree 


def creat_request(page):
    url = "https://51cg9.com/category/rdsj/"

    headers ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Cookie":"_ga=GA1.1.1237002539.1689828745; _ga_P6HKH41365=GS1.1.1689886432.2.1.1689886434.58.0.0",
    }

    #构造请求信息
    context = requests.get(url=url, headers=headers)
    content = context.text

    return content

def get_conent(content):
    #构造xpath语句
    tree = etree.HTML(content)

    #获取文章标题
    title = tree.xpath("//article//a//h2[@class='post-card-title']/text()")
    #获取文章链接
    links = tree.xpath('//article//a/@href')
    #遍历文章标题并去除多余的空白
    for i in range(len(title)):
        title[i] = title[i].strip()
        print(title[i])

    for i in range(len(links)):
        links[i] = "https://51cg9.com/category/rdsj/"+ links[i]
        print(links[i])

    #将文章标题和连接写入文档
    with open("51_chigua.txt",'a',encoding='utf-8') as f:
            for title,links in zip(title,links):
                f.write(f"{title}\t{links}\n")


""" 程序入口 """
if __name__== '__main__':
    #一共58页内容
    for page in range(59):
        content = creat_request(page)
        get_conent(content)
   


