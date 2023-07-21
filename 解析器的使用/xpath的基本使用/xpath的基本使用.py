from lxml import etree
import lxml.etree

"""  
    xpath解析
        1. 本地文件                                          etree.parse()
     ***2. 服务器响应的数据 response.read().decode('utf-8)    etree.HTML()

"""

#解析本地文件
tree = etree.parse('xpath的基本使用.html')

#tree.xpath('xpath路径')

"""  
    路径查找
        //: 查找所有子孙节点 不考虑层级关系
        /: 找直接子节点

"""

#查找ul下面的li
li_list = tree.xpath('//ul/li')
#判断列表长度
print(li_list)


"""  
    谓词查询
        //div[@id]
        //div[@id='maincontent']

"""
#查找所有带id的li标签
# text()获取标签中的内容
li_id = tree.xpath('//ul/li[@id]/text()')
print(li_id)


#查找id为1的标签    注意引号问题
li_id_1 = tree.xpath('//ul/li[@id="1"]/text()')
print(li_id_1)


"""  
    属性查询
        //@class

"""
#查找到id为li的li标签的class的属性值
li = tree.xpath('//ul/li[@id="1"]/@class')
print(li)


"""  
    模糊查询
        //div[contains(@,'he)]
        //div[starts.with(@id,'he')]
"""
#查询idli包含l的标签
li_id_l = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_id_l)

#查询id的值以c开头的li标签
li_id_c_2 = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(li_id_c_2)


"""  
    逻辑运算
        //div[@id="head" and @class="s_down"]
        //title | //price

"""
#查询id为li和class为c1的数据
li_id_class= tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
print(li_id_class)

li_2 = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
print(li_2)