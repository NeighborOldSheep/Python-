from bs4 import BeautifulSoup

#解析本地文件来讲解bs4 基础语法讲解

#默认编码格式是gbk 打开文件的时候需要指定编码形式
soup = BeautifulSoup(open('index.html',encoding='utf-8'),'lxml')


#根据标签名查找节点
""" 注意: 找到的是第一个符合条件的数据 """
print(soup.a)

#获取标签的属性和属性值
print(soup.a.attrs)
print("------------函数讲解-------------")

#bs4的函数
"""  
    三个函数
        1. find
            返回是第一个符合条件的数据

        2. find_all
            返回的是一个列表，并返回了所有的a标签

        3. select
"""

print('---------find函数------------')
#find函数
""" 返回是第一个符合条件的数据 """
print(soup.find('a'))

#根据title的值来找到对应的标签对象
print(soup.find('a',title='a2'))

#根据class的值来找到对应的标签对象  注意的是class需要添加下划线
print(soup.find('a',class_='a1'))




print('-------------find_all函数----------')
#find_all函数
""" 返回的是一个列表,并返回了所有的a标签 """
print(soup.find_all('a'))

#如果想获取的是多个标签的数据，那么需要在find_all的参数中添加的是列表的数据
print(soup.find_all(['a','span']))

#获取所有的li   limit的作用是查找前几个数据
print(soup.find_all('li',limit=2))


print('---------------select函数---------------')
#select函数
""" select方法返回的是一个列表,并且会返回多个数据 """
print(soup.select('a'))

#类选择器 可以通过 . 代表class
print(soup.select('.a1'))

#id选择器
print(soup.select('#l1'))

#属性选择器     通过属性来寻找对应的标签
#查找到li标签中有id的标签
print(soup.select('li[id]'))


#查找到li标签中id为l2的标签
print(soup.select('li[id="l2"]'))



print('---------------层级选择器--------------')

#层级选择器

#后代选择器

#找到div下面的li
print(soup.select('div li'))

#子代选择器
#某标签的第一级子标签
#注意: 很多的的计算机编程语言中  如果不加空格不会输出内容  但是在bs4中不会报错 会显示内容
print(soup.select('div > ul > li'))

#找到a和li标签的所有对象
print(soup.select('a,li'))


print('----------节点信息-----------')

#节点信息模块

#获取节点内容
obj = soup.select('#d1')[0]
"""
如果标签对象中  只有内容那么string和get_text()都可以使用； 
如果标签对象中除了内容还有标签  那么string获取不到数据 而get_text()是可以获取数据的 
    一般推荐get_text()
"""
print(obj.string)
print(obj.get_text())


print('---------------节点属性---------')

#节点的属性

obj = soup.select('#p1')[0]
#标签名字
print(obj.name)
#将属性值作为一个字典返回
print(obj.attrs)

#获取节点的属性
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])