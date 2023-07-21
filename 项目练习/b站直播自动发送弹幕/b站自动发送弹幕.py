#%%
import requests
import time
import tkinter as tk


danMu_list = ["想跟大家一起学习的小伙伴点个关注一起加油",
             "坐久了起来活动活动，别忘记喝点水呀",
            "粉丝牌子灰了送个免费的小心心就好啦",
            "牌子灰掉了送一个小心心就好啦！",
            "现在有点晚啦，大家加油，困了的就早点休息吧！",
            "如遇非善意发言可等待房管处理，请勿对线",
            "学习时间请少聊天，多多互相加油鼓励",
            "手机端的个人简介点头像再点更多主播信息",
            "如何打卡和查询积分请看直播间的左上角",
            "大家学习加油呀，不要放弃，成功就在前方"]



def send_danmu():
    #计数器
    flag = 0

    while True:
        time.sleep(2)
        #这个url是b站直播间发送弹幕api
        url = "https://api.live.bilibili.com/msg/send"
        #弹幕发送的信息
        send_msg = danMu_list[flag]
        #直播间房间号
        roomid = 8397302
        #生成当前时间
        ti = int(time.time())
        data = {
                "bubble": "0",
                "msg": send_msg,
                "color": "5816798",
                "mode": "1",
                "fontsize": "25",
                "rnd":"{}".format(ti),           #生成当前是时间
                "roomid": "{}".format(roomid),   #房间号
                "csrf": "559b7ce0c575b751c41e19edac401040",
                "csrf_token": "559b7ce0c575b751c41e19edac401040"
            }

        headers = {
                "cookie" : "_uuid=7C3CE5C6-8031-479D-E28C-DC09108C3C1E49198infoc; buvid3=650FC102-FC25-43A8-82BD-66DCB24494B6143075infoc; LIVE_BUVID=AUTO2216083104454562; CURRENT_FNVAL=80; blackside_state=1; buivd_fp=650FC102-FC25-43A8-82BD-66DCB24494B6143075infoc; buvid_fp_plain=650FC102-FC25-43A8-82BD-66DCB24494B6143075infoc; rpdid=|(uYJJkm~RJl0J'uY|)JYu~uY; dy_spec_agreed=1; buvid_fp=650FC102-FC25-43A8-82BD-66DCB24494B6143075infoc; fingerprint3=4d70ad72eea3ebc52931dbddc4ec512b; fingerprint_s=915f680eb0f7d49173d9ddf9a58f969b; CURRENT_BLACKGAP=1; CURRENT_QUALITY=80; bp_video_offset_113208720=553659157480125290; _dfcaptcha=a3063d6ea1bd148c8309157445b2c5f7; bsource=search_google; fingerprint=c2e0812177cb690d8466eb82677e2329; SESSDATA=8e8c1858%2C1643301881%2C15c4f%2A81; bili_jct=559b7ce0c575b751c41e19edac401040; DedeUserID=113208720; DedeUserID__ckMd5=e277ba287321bc10; sid=55s88q2o; bp_t_offset_113208720=553669469698781823; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1627318816,1627501925,1627748217,1627750413; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1627750413; PVID=10",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                'origin': 'https://live.bilibili.com'
            }

        response = requests.post(url=url,  data = data, headers=headers)

        #发送弹幕的索引自增
        flag += 1
        

        if flag >= 10:
            #发送完所有弹幕，冷却30分钟
            time.sleep(1800)
            #当索引超出值以后，从零开始发送弹幕
            flag = 0


send_danmu()
# %%
