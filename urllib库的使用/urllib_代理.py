import urllib.request 


url = 'https://www.baidu.com/s?wd=ip'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

proxies = {
    'http' : '121.13.252.62:41564'
}

# handler build_opner open
handler = urllib.request.ProxyHandler(proxies = proxies)
opner = urllib.request.build_opener(handler)

response = opner.open(request)

content = response.read().decode('utf-8')

with open('practice/ip_page.txt','w',encoding='utf-8') as f:
    f.write(content)