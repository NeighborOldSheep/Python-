from selenium import webdriver
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#元素定位

# 打开网页
driver.get("https://www.example.com")

# 通过 ID 查找元素
element_by_id = driver.find_element(by="id", value="element-id")

# 通过 name 查找元素
element_by_name = driver.find_element(by="name", value="element-name")

# 通过 class name 查找元素
element_by_class = driver.find_element(by="class name", value="element-class")

# 通过 CSS selector 查找元素
element_by_css = driver.find_element(by="css selector", value="element-css-selector")

# 通过 XPath 查找元素
element_by_xpath = driver.find_element(by="xpath", value="element-xpath")

# 关闭浏览器
driver.quit()