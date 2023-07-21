#使用urllib获取bilibli首页的源码
import urllib.request 


# (1)定义一个url 访问的地址
url = 'https://www.bilibili.com'

# (2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# (3)获取响应中的页面源码
# read方法 放回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制 --> 字符串     解码 decode('编码格式')
content = response.read().decode('utf-8')

# (4)打印数据
print(content)