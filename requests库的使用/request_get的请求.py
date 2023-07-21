"""  
    urllib:
        (1)一个类型以及六个方法
        (2)get请求
        (3)post请求 百度翻译
        (4)ajax的get请求
        (5)ajax的post请求
        (6)cookie登录   绕过登录进入到个人信息页面
        (7)代理     构造代理池

        

    requests:
        (1)一个类型以及六个属性
        (2)get请求
        (3)post请求 
        (4)代理
        (5)cookie   验证码
"""

import requests


url = 'http://www.baidu.com/s?'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

data = {
    'wd' : '北京'
}

"""  
    三个参数:
        url 请求资源路径
        params 参数
        kwargs 字典
总结:
    1.参数使用params传递
    2.参数无序urlencode编码
    3.不需要请求对象定制
    4.请求资源路径中的 ? 可以加也可以不加
        
"""
response = requests.get(url=url,params=data,headers=headers)
response.encoding = 'utf-8'
content = response.text
print(content)