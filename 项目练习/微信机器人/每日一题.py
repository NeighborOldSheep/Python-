""" from wxauto import WeChat

# 获取当前微信客户端
wx = WeChat()
 
# 获取会话列表
wx.GetSessionList()
 
with open("question1.txt","r",encoding="utf-8")as f:  #这个.txt里写要发送的文字
    for line in f.readlines():
        who = 'AP Noteable' #这里填要发送的人的备注
        wx.ChatWith(who)
        wx.SendMsg(line)
 """


"""
实现自动发送消息
"""
 
import time
import pyautogui as pg
import pyperclip as pc
import schedule


def send_msg():
    """
    定时发送信息给微信联系人
    """
    # 这里是微信联系人名字，或者群名称都可以
    name = ['AP Noteable', '文件传输助手','杨璐璐']
    msg = ['Hi,这是自动发送邮件工具，调试哦！', '晚上好呀！',  '各位抱歉，调试结束，给您带来不便，深表歉意！']
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


# 每天定时发送消息给固定的人
schedule.every().day.at("18:30").do(send_msg)

while True:
    schedule.run_pending()
    time.sleep(1)