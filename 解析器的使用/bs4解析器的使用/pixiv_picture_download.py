"""  
    
https:\/\/embed.pixiv.net\/decorate.php?illust_id=106038474
https://embed.pixiv.net/decorate.php?illust_id=106038474

"""

import urllib.request
from bs4 import BeautifulSoup

url = "https://i.pximg.net/img-master/img/2023/03/09/00/23/53/106038474_p0_master1200.jpg"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'referer':'https://www.pixiv.net/artworks/106038474'
}

request = urllib.request.Request(url=url,headers = headers)
response = urllib.request.urlopen(request)
content = response.read()

#使用bs4来寻找图片的json文件
with open('pixiv.png','wb') as fp:
    fp.write(content)


print(content)