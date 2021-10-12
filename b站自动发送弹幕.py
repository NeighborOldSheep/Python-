#%%
import requests
import time 
import random

danMu_List = ["想跟大家一起学习的小伙伴点个关注一起加油",
             "坐久了起来活动活动，别忘记喝点水呀",
            "粉丝牌子灰了送个免费的小心心就好啦",
            "牌子灰掉了送一个小心心就好啦！",
            "现在有点晚啦，大家加油，困了的就早点休息吧！",
            "如遇非善意发言可等待房管处理，请勿对线",
            "学习时间请少聊天，多多互相加油鼓励",
            "手机端的个人简介点头像再点更多主播信息",
            "如何打卡和查询积分请看直播间的左上角",
            "大家学习加油呀，不要放弃，成功就在前方"]


def send_Danmu():
    #索引
    index = 0

    while True:
        time.sleep(2)
        #b站弹幕api url
        url = "https://api.live.bilibili.com/msg/send"
        #获取弹幕信息
        send_msg = danMu_List[index]
        #获取当前时间
        ti = int(time.time())
        #直播间的id
        roomid = "21911052"

        data = {
            "bubble": "0",
            "msg": send_msg,              #弹幕内容
            "color": "5816798",     
            "mode": "1",
            "fontsize": "25",
            "rnd":"{}".format(ti),             #发送时间
            "roomid": roomid,           #直播id
            "csrf": "自己的csrf",
            "csrf_token": "自己的token"
        }

        headers = {
            "user-agent": "自己的agent",
            "cookie": "自己的cookie",
            "origin": "https://live.bilibili.com"
        }

        result = requests.post(url = url, headers = headers, data = data)

        #索引自增
        index += 1

        #判断弹幕信息是否全部发送完毕，如果发送完毕则进入冷却状态
        if index >= 10:
            #冷却30分钟
            time.sleep(1800)
            #弹幕信息归零，重头开始
            index = 0

send_Danmu()

  
# %%
