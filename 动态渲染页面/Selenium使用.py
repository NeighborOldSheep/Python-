#%%
from selenium import webdriver
import time

#打开浏览器
browser = webdriver.Chrome()

browser.get("https://www.baidu.com/")

#获取搜索框
input_first = browser.find_element_by_id("kw")
input_first.send_keys("Iphone")
time.sleep(1)
#点击搜索
button = browser.find_element_by_id("su")
button.click()
time.sleep(2)
browser.close()

# %%
