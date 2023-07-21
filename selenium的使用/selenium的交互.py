from selenium import webdriver
import time

browser = webdriver.Chrome()


#url
url = 'https://www.jd.com/?country=USA'
browser.get(url)

time.sleep(2)

#获取文本框对象
input = browser.find_element(by='id',value='key')

#在文本框中输入iphone14
input.send_keys('iphon14')
time.sleep(2)

#获取京东点击按钮
button = browser.find_element(by='css selector',value='button.button')
button.click()
time.sleep(2)

#滑到最下面
js_bottom = 'document.documentElement.scrollTop=10000000'
browser.execute_script(js_bottom)
time.sleep(2)

#回到上一页
browser.back()
time.sleep(2)

#回去
browser.forward()
time.sleep(3)

#退出
browser.quit()