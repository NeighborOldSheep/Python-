import jsonpath
import json 
import urllib.request 

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1678303143789_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    #'accept-encoding': 'gzip, deflate, br,utf-8',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'bx-v': '2.2.3',
    'cookie': 't=a71af6038b14ce0e6303d07dbcd3b57c; thw=us; cna=1/VjGHgKXQ4CAWFaJBuhYlkp; cookie2=1edb65281f1c9f82b4992580ec3a7cc3; v=0; _tb_token_=f336eeb1b17e6; xlly_s=1; isg=BIOD9JNL4-KeG6grYB2jWf7yEkct-Bc6HfQWy7VhN-JZdKGWPchxihxi7hw6VG8y; tfstk=c2tlB7Vp6U778HopGQsSjkp4ot0OZ_rFsH8w0xaSmSDPyTxVifU47phSn9hsay1..; l=fBjJc6tnT_stlVhwBO5Clurza77T1IdbzsPzaNbMiIEGa6sdtFicwNCs6LmwSdtjQTfcwetrl5ZFzdn6JO4LggiMW_N-1NKmsYpw-bpU-L5..',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',        
    }

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

#split切割
content  = content.split('(')[1].split(')')[0]

with open('淘票票.json','w',encoding='utf-8') as f:
    f.write(content)

obj = json.load(open('淘票票.json','r',encoding='utf-8'))

#使用jsonpath解析本地json数据
region_list = jsonpath.jsonpath(obj,'$..regionName')

print(region_list)
for i in range(len(region_list)):
    print(region_list[i])