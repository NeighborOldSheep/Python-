#%%
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json

def get_page(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None 

def parse_page(html):
    soup = BeautifulSoup(html,'lxml')
    li = soup.select(".rank-item")
    #print(li)
    for top_anime in li:
        yield{
            "排名" : top_anime.select(".num")[0].get_text(),
            "番剧名" : top_anime.select(".title")[0].get_text(),
            "更新状态" : top_anime.select(".pgc-info")[0].get_text(),
            #由于.detial里面有很多个class相同的span标签下标[0]的才是代表播放量的所以这里下标为0(以此类推)
            "播放量" : top_anime.select(".detail>span")[0].get_text().strip()
        }

def write_file(content):
    with open("top_anime.txt", "a", encoding = "utf-8") as f:
        f.write(json.dumps(content, ensure_ascii = False) + "\n")
        
               


def main():
    url = "https://www.bilibili.com/v/popular/rank/bangumi"
    html = get_page(url)
    for top_anime in parse_page(html):
        print(top_anime)
        write_file(top_anime)
    

main()



# %%
