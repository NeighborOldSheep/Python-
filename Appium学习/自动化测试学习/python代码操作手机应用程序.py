from appium import webdriver

#1.设置终端设置
desired_caps = {
  'platformName': 'Android',
  'deviceName': 'xxx',
  'platformVersion': '6.0.1',
  'appPackage': 'com.tencent.mm',
  'appActivity': 'com.tencent.mm.ui.LauncherUI',
  'automationName': 'UiAutomator2',
  "noRest" : True
 }

#2.appium server进行启动

#3.发送指令给appium server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#确认模拟机/手机 能够被电脑识别 ---> 使用adb命令 adb devices