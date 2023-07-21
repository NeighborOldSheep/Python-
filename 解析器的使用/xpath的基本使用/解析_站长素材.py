import urllib.request 
from lxml import etree 


#(1)请求对象定制
def create_request(page):
    # https://sc.chinaz.com/tupian/qinglvtupian.html
    # https://sc.chinaz.com/tupian/qinglvtupian_2.html
    """ 由于该网站第一页跟后面页码的网址结构不同通过if判断是第几页 """
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
       
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_{}.html'.format(page)
       
    #构造request请求方法
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    request = urllib.request.Request(url=url,headers=headers)

    #返回request请求方法
    return request

#(2)获取网页源码
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    #返回网页源码
    return content

#(3)下载
def down_pic(content):
   
    #构造xpath路径获取图片中src地址
    tree = etree.HTML(content)
    #获取图片的名称
    img_name = tree.xpath('//img[@class="lazy"]/@alt')
    #返回的是 src路径在列表里面
    #如果是运用懒加载的话 xpath匹配的是懒加载之前的src数据！！！！
    src_list = tree.xpath('//img[@class="lazy"]/@data-original')
    #print(img_name)
    #遍历列表src 拼接https下载图片
    for i in range(len(src_list)):
        url_img = 'https:' + src_list[i]
        urllib.request.urlretrieve(url=url_img,filename='practice/couple_img_' + str(img_name[i]) + '.jpg')

#需求:下载前十页图片
if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_pic(content)