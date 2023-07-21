import requests


url = 'https://www.baidu.com'

response = requests.get(url=url)

#一个类型和六个属性
""" Response类型的 """
print(type(response))


#设置响应的编码格式
response.encoding = 'utf-8'

#以字符串的形式 返回了网页的源码
print(response.text)

#返回一个url地址
print(response.url)

#以二进制的方式返回数据
print(response.content)

#返回响应的状态码
print(response.status_code)

#返回响应头
print(response.headers)