import requests
from lxml import etree

url = 'https://www.uukanshu.com/b/29676/181197.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

response = requests.get(url=url,headers=headers)

tree = etree.HTML(response.text)
text = tree.xpath('//div[@id="contentbox"]/text()')
content = ''.join(text)
print(content)


""" import qrcode

# 定义 URL
url = "https://forms.gle/UGtHiNygnLxvXVoh7"

# 生成二维码图像
img = qrcode.make(url)

# 保存图像
img.save("google_form.png")
 """