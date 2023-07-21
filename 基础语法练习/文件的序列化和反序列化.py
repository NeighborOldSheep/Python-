"""  
    对象 --》 字节序列 == 序列化
    字节序列 --》 对象 == 反序列化

"""
""" 
fp = open('test.txt','w')
#默认情况我们只能将字符串写入文件中
fp.write('hello world')
fp.close() """

""" fp = open('test.txt','w')
name_list = ['zhangsan','lisi']
#如果是一个对象，无法写入文件中 如果想写入文件必须使用序列化操作
fp.write(name_list) """

import json

#序列化的两种方式

#dumps()

""" #(1)创建一个文件
fp = open('test.txt','w')
#(2)定义一个列表
name_list = ['zs','li']

#序列化
#将 python对象变成 json字符串
names = json.dumps(name_list)
#将names写入文件中
fp.write(names)
fp.close() """


#dump
""" #再将对象转换为字符串的同时 指定一个文件的对象 把转换后的字符串写入到这个文件里
fp = open('test.txt','w')
name_list = ['zs','li']
#相当于 names = json.dumps(name_list) 和 fp.write(names)
json.dump(name_list,fp)
fp.close()
 """


#反序列化
#将一个json的字符串 变成 一个python对象

fp = open('test.txt','r')
content = fp.read()

#loads
#将json字符串变成python对象
""" 
result = json.loads(content)
print(type(result)) 
"""

#load
fp = open('test.txt','r')
result = json.load(fp)
print(type(result))