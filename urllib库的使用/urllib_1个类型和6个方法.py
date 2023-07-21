import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# response 是 HTTPResponse的类型
#print(type(response))

# 一个类型和6个方法

#按照一个字节一个字节的去读
""" 
content = response.read()
print(content) 
"""

#返回多少个字节
""" 
content = response.read(5)
print(content)
"""

#读取一行
""" 
content = response.readline()
print(content)
"""

#读取多行
""" 
content = response.readlines()
print(content)
"""
#返回状态码  200正面没问题 
""" print(response.getcode()) """

#返回url地址
""" print(response.geturl()) """

#获取状态信息
""" print(response.getheaders()) """

#一个类型 HTTPResponse
"""  
    六个方法:
        read()
        readline()
        readlines()
        getcode()
        geturl()
        getheaders()
"""