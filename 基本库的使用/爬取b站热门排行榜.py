#%%
import requests
from requests.exceptions import RequestException
import re
import json

#抓取网页源码
def get_page(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            #网页能够正常访问返回网页源码
            return response.text
        else:
            return None
    except RequestException:
        return None


#提取网页所需内容
def parse_page(html):
    pattern = re.compile('<li.*?data-rank="(\d+)".*?>.*?<a.*?class="title">(.*?)</a>.*?'+
                        '<i class=".*?play"></i>.*?(.*?)</span>.*?'+
                        '<i class=".*?view"></i>.*?(.*?)</span>.*?'+
                        '<i class=".*?author"></i>>*?(.*?)</span>',re.S)
    items = re.findall(pattern,html)
    #print(items)
    for item in items:
        yield{
            "排名" : item[0],
            "作品名" : item[1].strip(),
            "播放量" : item[2].strip(),
            "弹幕量" : item[3].strip(),
            "UP主" : item[4].strip()
        }

#写入文件
def write_to_file(content):
    with open('bilibli_top_100_video.txt','a',encoding="utf-8") as f:
        #ensure_ascii=False可以保证输出结果是中文形式而不是unicode编码形式
        f.write(json.dumps(content,ensure_ascii=False)+"\n")


def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)
main()
# %%
