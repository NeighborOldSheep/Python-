# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象
browser = webdriver.Chrome()

# (3)访问网站
url ='https://www.jd.com/?country=USA'

browser.get(url)

#获取网页源码
content = browser.page_source
print(content)