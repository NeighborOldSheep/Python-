import urllib.request 

#需求 使用handler来访问百度 获取网页源码

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)


#handler build_opner open

#(1)获取handler对象
handler = urllib.request.HTTPHandler()

#(2)获取opner对象
opner = urllib.request.build_opener(handler)

#(3)调用open方法
response = opner.open(request)

content = response.read().decode('utf-8')

print(content)