import urllib.request 
import urllib.parse

#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

#需求  获取https://www.baidu.com/s?wd=周杰伦网页源码

url = 'https://www.baidu.com/s?wd='

#请求对象定制为了解决反爬的第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

#将周杰伦三个字变成unicode编码的格式
#我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')

#拼接网址
url = url + name

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器服务器发送请求
resposne = urllib.request.urlopen(request)

#获取响应内容
content = resposne.read().decode('utf-8')

print(content)