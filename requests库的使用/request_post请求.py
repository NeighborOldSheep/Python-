import requests
import json 

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

data = {
    "kw" : "love"
}

#url    请求地址
#data   请求参数
#kwargs 字典
"""  
    总结:
        1.post请求时不需要编解码的
        2.post请求的参数是data
        3.不需要请求对象的定制
"""
response = requests.post(url=url,data=data,headers=headers)
content = response.text 
obj = json.loads(content)
print(obj)