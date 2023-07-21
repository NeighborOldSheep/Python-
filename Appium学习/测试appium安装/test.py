from appium import webdriver

desired_caps = {
  'platformName': 'Android',
  'deviceName': 'xxx',
  'platformVersion': '6.0.1',
  'appPackage': 'com.tencent.mm',
  'appActivity': 'com.tencent.mm.ui.LauncherUI'
 }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 