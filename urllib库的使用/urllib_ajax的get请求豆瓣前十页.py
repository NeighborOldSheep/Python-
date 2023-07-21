import urllib.request
import urllib.parse
import json 

#url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&actio'
#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=100&limit=20

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start' : (page-1)*20,
        'limit' : 20
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Cookie': 'bid=K2Ho__GvqKc; _ga=GA1.2.654365133.1678150726; _gid=GA1.2.662897909.1678150726; ll="108288"; __utma=30149280.654365133.1678150726.1678150742.1678150742.1; __utmb=30149280.0.10.1678150742; __utmc=30149280; __utmz=30149280.1678150742.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.654365133.1678150726.1678150742.1678150742.1; __utmb=223695111.0.10.1678150742; __utmc=223695111; __utmz=223695111.1678150742.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1678150742%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __gpi=UID=000009580cb6d1b6:T=1678150743:RT=1678150743:S=ALNI_MaHFqSVcW2HXSMo6roUy3gQPg1sMQ; ucf_uid=22f6f05a-ae5f-4078-9687-ef26e22bd01f; __gads=ID=37db33d377d30469-22f7835db9db00d2:T=1678150743:S=ALNI_MZj3oDyODIxNonEDHXB-L5MfBXV5w; _pbjs_userid_consent_data=3524755945110770; cto_bundle=Cwb8GV9VWDAxWWx3SVVhUmc5ZyUyRjAxNmJpVHA0VXlnRVJaRWFtYndtZmdLMjFWY3RCaDVEOGxxU1lYSE9EcWhUbSUyRmlCZTRycjNaUUxEbVlNUXIzck1LUnZ5UWVsemNqaWwlMkZicHhtY1huaFREZGVlS09mRzUlMkJDVmFCdjJQQzkzMCUyQnBVVGxodU9peU5jdlBvanhyUUoxeEFRQnVRJTNEJTNE; cto_bidid=LBDel181Y2FnVmkwbnJpdmMlMkZ1SjF2dlBvY0daY2t2TEtJODI5d2xBQU5IY2dnc3R5dHcybzZ2JTJGQ1oyRkRvU080VWVVVzhoSDdQUUtpTWVKT2liRTJEdERtMU5YaFg4MDZkNjZoUHltMnBvS2lnUjglM0Q; _pk_id.100001.4cf6=edf2a62e51f056c2.1678150742.1.1678151778.1678150742'
    }

    data = urllib.parse.urlencode(data)
    url = base_url + data 
    
    request = urllib.request.Request(url=url,headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content 

def down_load(page,content):
    with open('douban_' + str(page) +'.json','w',encoding='utf-8') as f:
        f.write(content)



#程序如果
if __name__ == '__main__':
    start_page = int(input('起始的页码'))
    end_page = int(input('请输入结束的页码'))
    for page in range(start_page,end_page+1):
        #每一页都有个自己的请求对象的定制
        request = create_request(page)
        content = get_content(request)
        #下载数据
        down_load(page,content)

