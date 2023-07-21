import requests
from lxml import etree

for page in range(1,9):
    url = 'http://wap.csres.com/sort/Chtype/F01_{}.html'.format(page)

    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    html_str  = requests.get(url,headers = ua).text

    #转类型， 转成我们xpath能够获取到数据的类型
    xpath_str = etree.HTML(html_str)
    #通过xpath语法获取整个表格:   //thead[@class='th1']/tr
    tr_list = xpath_str.xpath('//thead[@class="th1"]/tr')

    #print(tr_list)


    for tr in tr_list:
        if tr.xpath('.//td[1]/a/font/text()'):
            #标准编号
            number = tr.xpath('.//td[1]/a/font/text()')[0]
            #标准名称
            name = tr.xpath('.//td[2]/a/font/text()')[0]
            #发布部门
            department = tr.xpath('.//td[3]/font/text()')[0].strip()
            #实施日期
            time = tr.xpath('.//td[4]/font/text()')[0]
            #状态
            status = tr.xpath('.//td[5]/font/text()')[0]
            #print(num)
        
            #保存语法  追加  wb: 二进制数据  音频,图片,视频
            with open('数据表格.csv','a+',encoding='utf-8-sig') as file:
                file.write('{},{},{},{},{}\n'.format(number,name,department,time,status))
                print(name+"下载完成")