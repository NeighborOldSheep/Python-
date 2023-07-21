from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree
import urllib.request

#创建浏览器对象
browser = webdriver.Chrome()

url = 'https://www.douyin.com/user/MS4wLjABAAAAVIBzKeBtUqVjI4bb99Hqqpf5Hs1OYw7UePx7N12Z4H3VB847_cCqdf0XcD-_86AH'

browser.get(url)

#睡眠5s过验证码
time.sleep(15)

#获取源码
if browser.find_element('xpath','//div[@class="_bEYe5zo"]'):
    content = browser.page_source 
    #print(content)

else:
    time.sleep(5)
    content = browser.page_source 
    #print(content)

#点击第一个视频
time.sleep(2)
a_list = browser.find_element('xpath','//ul[@class="EZC0YBrG"]/li//a[@class="B3AsdZT9 chmb2GX8"]')
a_list.click()
time.sleep(1)


#下一条视频
""" next_video = browser.find_element('xpath','//div[@id="root"]')
next_video.send_keys(Keys.ARROW_DOWN).perform() """

#获取视频的下载地址
video_src = browser.find_element('xpath','//div[@class="S6T7oCND slider-video"]//xg-video-container[@class="xg-video-container"]/video/source[1]')
video_src = video_src.get_attribute('src')
#获得视频名称
video_name = browser.find_element('xpath','//div[@class="video-info-detail"]//span[@class="e_h_fqNj"]')
video_name = video_name.text
time.sleep(1)



urllib.request.urlretrieve(url=video_src,filename=str(video_name)+'.mp4')



