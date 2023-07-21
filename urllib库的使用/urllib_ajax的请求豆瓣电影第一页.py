import urllib.request
import urllib.parse

#get请求
#获取豆瓣电影的第一页数据 并保存起来

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&actio'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

# (1)请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# (2)获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

#数据下载
# open方法默认情况下使用gbk的编码 如果想要保存汉字或者中文 需要在open方法中来指定编码格式为utf-8
with open('douban.json','w',encoding='utf-8') as f:
    f.write(content)