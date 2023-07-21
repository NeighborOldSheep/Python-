#适用的场景: 数据采集时 需要绕过登录 然后进入到某个页面
#个人信息页面是utf-8 但是还是报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登录页面
#那么登录页面不是utf-8编码 所以报错

import urllib.request 


url = 'https://user.qzone.qq.com/1377264163/infocenter'

headers = {
    'cookie': 'ptui_loginuin=1377264163; uin=o1377264163; skey=@GHeJIiTRb; RK=I9sYxJjdci; ptcz=8c8d0070aab4b0be2073aaa4bf53c5aece9188fe173b3c7edb1d9e2189f68482; p_uin=o1377264163; pt4_token=g0lscTtJ1NbuYynuAW2dRAX2trq5BDzhN13dc-G8yAM_; p_skey=FB93X1Q-NOknRGAeOsnKt8zhzySmmXnQhwgH3bq*BR8_; qz_screen=2560x1080; __layoutStat=7; pgv_pvid=5147478740; pgv_info=ssid=s7915694701; QZ_FE_WEBP_SUPPORT=1; rv2=800E0BBF12B78D4876948144221802538C3391A0A3009BFE9E; property20=718099004208461BE31834A474262804DC935420164F3A4720A6B1DE8E14C59D1896D52204730B36; cpu_performance_v8=9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)