""" 
Desired Capabilites-Appium 自动化配置

设置参数:
    操作系统    platformName
    版本        platformVersion 
    设备名称    
    应用程序
    入口启动页面
 """
desired_caps = {
  'platformName': 'Android',
  'deviceName': 'xxx',
  'platformVersion': '6.0.1',
  'appPackage': 'com.android.settings',
  'appActivity': 'com.android.settings.Settings',
  "noReset" : True
}