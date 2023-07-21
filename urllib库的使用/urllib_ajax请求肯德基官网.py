import urllib.request 
import urllib.parse 


#http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
"""  
data第一页

cname: 北京
pid: 
pageIndex: 1
pageSize: 10

data第二页
cname: 北京
pid: 
pageIndex: 2
pageSize: 10

"""
def creat_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex' : page,
        'pageSize': '10'
    }
    #给data编码
    data = urllib.parse.urlencode(data).encode('utf-8')
   

    #构造request
    reuqest = urllib.request.Request(url=base_url,headers=headers,data=data)

    return reuqest 

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content

def download_info(page,content):
    with open('KFC_Beijing_location' + str(page) + '.json','w',encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page):
        request = creat_request(page)
        content = get_content(request)
        #下载
        download_info(page,content)