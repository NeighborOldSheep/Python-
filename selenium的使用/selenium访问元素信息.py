from selenium import webdriver 


browser = webdriver.Chrome()

url = 'https://www.jd.com/?country=USA'
browser.get(url)

input = browser.find_element(by="id",value='key')
a = browser.find_element(by='class name',value='cate_menu_lk')
print(input.get_attribute('class'))
print(input.tag_name)
#获取的是元素文本
print(a.text)