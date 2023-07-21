""" 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com'
driver.get(url)

driver.save_screenshot('baidu.png')
 """

#封装handless
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)

    return browser

browser = share_browser()
url = 'https://www.baidu.com'

browser.get(url)