import urllib.request
import random

proxies_pool = [
    {'http' : '121.13.252.62:41564'},
    {'http' : '27.42.168.46:55481'}

]


proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

#handler build_opner open
handler = urllib.request.ProxyHandler(proxies = proxies)
opner = urllib.request.build_opener(handler)
response = opner.open(request)

content = response.read().decode('utf-8')

with open('practice/proxies_pool.txt','w',encoding='utf-8') as f:
    f.write(content)