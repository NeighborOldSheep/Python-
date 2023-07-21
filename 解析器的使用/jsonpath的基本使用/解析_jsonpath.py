import jsonpath
import json

with open('jsonpath.json','r',encoding='utf-8') as f:
    obj = json.load(f)
#书店所有的书的作者
""" jsonpath.jsonpath(对象,'jsonpath语法') """
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(author_list)

#获取所有的作者
all_author_list = jsonpath.jsonpath(obj,'$..author')
print(all_author_list)

#store下面的所有元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')
print(tag_list)

#store里面所有的钱
price_list = jsonpath.jsonpath(obj,'$..price')
print(price_list)

#获取第三本书
third_book = jsonpath.jsonpath(obj,'$..book[2]')
print(third_book)

#最后一本书
last_book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
print(last_book)

#获取前两本书
first_two_book = jsonpath.jsonpath(obj,'$..book[:2]')
print(first_two_book)

""" 条件过滤需要在圆括号前面添加一个 ？ """
#过滤出所有包含版本号的书
isbn = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(isbn)


#过滤出超过十块的书
book_price = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_price)