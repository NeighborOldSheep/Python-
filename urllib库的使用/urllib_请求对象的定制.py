import urllib.request

url = 'https://www.baidu.com'

#url的组成
"""  
    https://www.baidu.com/s?wd=周杰伦

    协议:   http/https   
    主机:   www.baidu.com
    端口号:  http 80   https 443   mysql 3306  orcale 1521 redis 6379  mangodb 27017
    路径    s
    参数    wd=周杰伦
    锚点    #

"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

#因为urlopen方法中不能存储字典 所以headers不能传递进去
#请求对象的定制
#注意 因为参数顺序的问题 不能直接写url 和 headers 中间还有一个data 所以需要使用关键字传参
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)