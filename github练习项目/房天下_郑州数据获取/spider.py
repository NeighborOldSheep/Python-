from lxml import etree
import requests 
import csv

def create_request(page):

    """ 构造请求头 并返回网页源码 """
    url = "https://zz.newhouse.fang.com/house/s/b9" + str(page) 
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }

    response = requests.get(url=url,headers=headers)

    content = response.text 

    return content


def get_content(content):
    """ 
        获取房屋信息
            1. 房屋名称
            2. 房屋大小(几室几厅)
            3. 房屋具体位置
            4. 房屋价格
    """

    #构造xpath
    tree = etree.HTML(content)

    #获取房屋名称
    house_name = tree.xpath('//ul//div[@class="nlc_details"]//div[@class="nlcd_name"]/a/text()')

    #获取房屋大小
    house_size = tree.xpath('//ul//div[@class="nlc_details"]//div[@class="house_type clearfix"]/text()[contains(., "—")]')

    #获取房屋具体位置
    house_address = tree.xpath('//ul//div[@class="nlc_details"]//div[@class="address"]/a/@title')

    #房屋每平米价格
    house_price = tree.xpath('//ul//div[@class="nlc_details"]//div[@class="price_fix"]//span/text()')

    #房屋信息
    house_info_list = []

    #遍历房屋名称 & 具体位置 & 每平米价格
    for i in range(len(house_name)-1):
        #去除多余的空格
        house_name[i] = house_name[i].strip()
        house_size[i] = house_size[i].strip()
        house_address[i] = house_address[i].strip()
        

        #检测价格是否是价格待定
        if house_price[i] == "价格待定":
            house_price[i] = house_price[i]
        #如果不是添加 元/m^2
        else:
            house_price[i] = house_price[i] + "元/每平方米"

        #把所有房屋信息添加到列表方便保存数据
        house_info = [house_name[i],house_size[i],house_address[i],house_price[i]]
        #每一个房屋信息为一个列表添加到总房屋列表
        house_info_list.append(house_info)


        print(house_name[i],house_size[i],house_address[i],house_price[i])

    return house_info_list

def save_to_csv(house_info_list):
    #保存房屋信息到csv文件
    with open("zhengzhou_house_info.csv","a",newline="",encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        #写入房屋信息
        for house_info in house_info_list:
            writer.writerow(house_info)


if __name__ == '__main__':
    with open("zhengzhou_house_info.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头
        writer.writerow(["房屋名称", "房屋大小", "房屋具体位置", "房屋每平米价格"])

    for page in range(11):
        content = create_request(page)
        house_info_list = get_content(content)
        save_to_csv(house_info_list)