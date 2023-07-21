""" 
    通过登录进入到主页面
        登录的时候需要的参数很多
    
__VIEWSTATE: rJ3/36k1f/aR4RCwx2CkaCRypqMZVNA8IKoCVtQZ7bIuYOyg1xuDltCr8fAvJXEt7kIxfuXB9NIamZB4KYg4IwBMLSZLToJMmLiQr/Oj0te7+5yX8JulaEPJCuZi5XP0OzTmeT3DZpSnvEFA++lJru7FGMU=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: coleyang2016@gmail.com
pwd: Yanghongchen@666
code: vya3
denglu: 登录


我们观察到 __VIEWSTATE  __VIEWSTATEGENERATOR  code 他们三个是一个可以变化的量

难点:
    1. __VIEWSTATE  __VIEWSTATEGENERATOR    一般情况下看不到的数据都是在页面的源码中
        观察到这两个数据在页面的源码中 所以我们需要获取页面的源码 然后进行解析就可以获取了

    2. 验证码

"""

import requests 
from bs4 import BeautifulSoup
import urllib.request

#这是登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

#获取页面源码
response = requests.get(url=url,headers=headers)
content = response.text

#解析页面源码   获取 __VIEWSTATE  __VIEWSTATEGENERATOR
soup = BeautifulSoup(content,'lxml')
#获取 __VIEWSTATE
viewState = soup.select('#__VIEWSTATE')[0].attrs.get('value')
#获取 __VIEWSTATEGENERATOR
viewGenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

""" 获取验证码图片 """
img_src = soup.select('#imgCode')[0].attrs.get('src')
#验证码图片地址拼接
code_url = 'https://so.gushiwen.cn' + img_src

""" 
    获取了验证码的图片之后 下载到本地然后观察验证码 
    观察之后然后在控制台 来输入这个验证码就可以将这个值 
        给code参数
"""

#有坑
#urllib.request.urlretrieve(url=code_url,filename='code.jpg')

#requests里面有一个方法叫做 session()  通过session的返回值 就能使请求变成一个对象

session = requests.session()
#验证码的url的内容
response_code = session.get(code_url)
#注意此时要使用二进制数据  因为要下载的是图片 所以要用二进制content
content_code = response_code.content
#wb的模式就是将二进制数据写入到文件
with open('code.jpg','wb') as f:
    f.write(content_code)

code_name = input('请输入你的验证码')


""" 登录 """
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE' : viewState,
    '__VIEWSTATEGENERATOR' : viewGenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'coleyang2016@gmail.com',
    'pwd': 'Yanghongchen@666',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url,headers=headers,data=data_post)
content_post = response_post.text

with open('gushiwen.html','w',encoding='utf-8') as f:
    f.write(content_post)


"""  
    难点:
        1. 隐藏域问题
        2. 验证码

"""