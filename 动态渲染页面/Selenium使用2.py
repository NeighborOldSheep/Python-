#%%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#获取浏览器
browser = webdriver.Chrome()
browser.get("https://live.bilibili.com/")

#声明等待时间
wait = WebDriverWait(browser,10)
#获取搜索框     显示等待;直到网页该元素加载出来
search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div.nav-ctnr > nav > div > div.right-part.h-100.f-right.f-clear > div.search-bar-ctnr.dp-table.h-100.f-left > form > div > input")))
search_input.send_keys("积极向上的骷髅")
time.sleep(1)

#获取点击按钮
button = wait.until(EC.element_to_be_clickable(By.CLASS_NAME,"search-btn"))
button.click()
# %%
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://live.bilibili.com/8397302?broadcast_type=0")
print(browser.page_source)

# %%
