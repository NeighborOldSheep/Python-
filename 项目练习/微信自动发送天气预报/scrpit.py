import requests 
from lxml import etree
import time
import pyautogui as pg
import pyperclip as pc


def send_msg(msg):
    """
    定时发送信息给微信联系人
    """
    # 这里是微信联系人名字，或者群名称都可以
    name = ['Cassia']
    msg = msg
    # self.msg = ['Hi, 坤少，这是一个test!', 'AMP接口人', 'AG业务专家']
    # 操作间隔为1秒
    pg.PAUSE = 1.5
    # 快捷键调出桌面微信客户端
    pg.hotkey('ctrl', 'alt', 'w')
    # 搜索栏
    pg.hotkey('ctrl', 'f')

    # 找到好友
    for dex in name:
        pc.copy(dex)
        # 粘贴
        pg.hotkey('ctrl', 'v')
        # 回车
        pg.press('enter')
        # 发送消息
        for i in msg:
            pc.copy(i)
            pg.hotkey('ctrl', 'v')
            pg.press('enter')
        # 搜索栏
        pg.hotkey('ctrl', 'f')

    # 隐藏微信
    time.sleep(1)
    pg.hotkey('ctrl', 'alt', 'w')


url = 'https://www.google.com/search?q=Monterey+Park+tempature'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'cookie':'CONSENT=YES+US.zh-CN+20161030-06-0; _ga=GA1.1.1669998921.1617764973; SID=UwgDZzA1BjzzxN85QnMfeYZ3mdLQrjr92u2rpnB8SgmOn4L6riFz6426j2iArK_l371Ldw.; __Secure-1PSID=UwgDZzA1BjzzxN85QnMfeYZ3mdLQrjr92u2rpnB8SgmOn4L65U3ytZjYsJ8bNA8kwIGmcw.; __Secure-3PSID=UwgDZzA1BjzzxN85QnMfeYZ3mdLQrjr92u2rpnB8SgmOn4L6_t1f8qJjSnYi2MWTUO2KLw.; HSID=AC3ppebP-ucepX7Lf; SSID=AVDfSQr3vvG8C-vsV; APISID=0oxPOT9e3Vx04ej4/AVzNhk-x9Ox3jBWLf; SAPISID=fYIQ9neA9RFg173j/AZuDGw3fjBZmNOZpy; __Secure-1PAPISID=fYIQ9neA9RFg173j/AZuDGw3fjBZmNOZpy; __Secure-3PAPISID=fYIQ9neA9RFg173j/AZuDGw3fjBZmNOZpy; OTZ=6961057_84_88_104280_84_446940; SEARCH_SAMESITE=CgQI9ZcB; AEC=AUEFqZdyuJqJ8ta1LpKRLdWZ9EsyU6E7vDk7XGMU3MHo59yVHFfmY4bCQc4; NID=511=WquHc0FYZhW6w9olROqCsnwExbgWAuHDQ3i58FuUAC7RJRDPmIIW4EJascngi2NUbdX93FHCysQ2Z3Zo29x9kMK58kRoh3BgOTbeklPdl0uutJ2dVEG3vQ__aJB0kxlp62zOrttzkZsMI2T9a7RGxXfI5rS2yTge0DDEDh32iCQ6KL1uWk2vQiPFQOxpN9I3CeKM-fFEReQMWWNTrUPDnYwfR-OaMReMw4a5Gl0zu4E5lxAAJp7RAHXpLN3DnWXOo3cdRMfNVUa9zfLM8ITSV5hw5PfCelMyII_Kx3atpprNFfqcpkbaWOf2rM9YTDDth8OTLWwSpjE; 1P_JAR=2023-03-31-18; DV=wxne0h1JXllcUFfdruUpeWrFTLKPc1gvJBy_9KrqZAAAAHCgB-4eMgw7EAEAAAQWt4oXwIq_hQAAAF_T6t0I-i0zIwAAAA; SIDCC=AFvIBn9UDUJ0lPkUz_BWijhK0GhNRrMXrv1xXSiOTzmTfXicel1606LuIbV7MQKe1EsUZbchEA; __Secure-1PSIDCC=AFvIBn-wFmtv9zrKcM2SgibH_qzQM7ng23n4q3e-rd3wrEnAu95nxTFvR5u2FuTWRWpZlke3At8; __Secure-3PSIDCC=AFvIBn-dqBSXuCQ18gdBRej2PXuxao4lyEQGv_Za8ECtG6HFHhAZQ3Dg2eFvUaBwIrxZkv_319E',
}

#获取网页源码
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
context = response.text

#构造xpath路径
tree = etree.HTML(context)
#获取 天气 最高最低温度
weather = tree.xpath('//div[@id="res"]//span[@id="wob_dc"]/text()')[0]
high_temp = tree.xpath('//div[@id="wob_d"]//div[@class="gNCp2e"]/span[2]/text()')[0]
low_temp = tree.xpath('//div[@id="wob_d"]//div[@class="QrNVmd ZXCv8e"]/span[2]/text()')[0]

#拼接发送信息
if int(high_temp) < 30 and int(high_temp) > 20:
    msg = ['今天Monterey Park天气' + str(weather) + '最高温度' + str(high_temp) + '度,' + '最低温度' + str(low_temp) + '度,完美的天气出去散步叭~' ]

elif int(high_temp) < 20:
    msg = ['今天Monterey Park天气' + str(weather) + '最高温度' + str(high_temp) + '度,' + '最低温度' + str(low_temp) + '度,天气比较凉记得带外套喔~' ]

elif int(high_temp) > 30:
    msg = ['今天Monterey Park天气' + str(weather) + '最高温度' + str(high_temp) + '度,' + '最低温度' + str(low_temp) + '度,天气炎热出门记得擦防晒!!!' ]

elif int(weather) == '阵雨':
    msg = ['今天Monterey Park天气' + str(weather) + '最高温度' + str(high_temp) + '度,' + '最低温度' + str(low_temp) + '度,今日有雨记得带伞！!!!' ]



#schedule.every().day.at("18:30").do(send_msg)
send_msg(msg)