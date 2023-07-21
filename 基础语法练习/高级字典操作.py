#字典的查询

#定义字典
person = {'name':'五千','age':28}

#访问person的name
print(person['name'])
print(person['age'])

#使用[]的方式 获取字典中不存在的key的时候  报错: KeyError: 'sex'
#print(person['sex'])

#不能使用 .的方式来访问字典的数据
#print(person.name)

print(person.get('name'))
print(person.get('age'))

#使用 . 的方式，获取字典中不存在key的时候 会返回一个None的值
print(person.get('sex'))





#字典的修改
human = {'name':'张三','age':18}

#修改之前的字典
print(human)

#修改name的值为法外狂徒
human['name'] = '法外狂徒'
print(human)




#字典添加
#如果使用变量名字['key'] = 数据时  这个key在字典中不存在那么就会变成新增键对值
person['sex'] = 'male'




#字典删除
""" 
    del
        (1)删除字典中指定的某一个元素
        (2)删除整个字典
    clear
        (3)清空字典 但是保留字典对象

"""
food = {'name':'汉堡','age':18}

#删除之前
print(food)

#删除之后
""" 
del food['age']
print(food) 
"""

#删除整个字典
""" 
del food 
print(food)

"""

#clear方法 清除所有字典数据 保留空字典
food.clear()
print(food)






#字典遍历
person1 = {'name':'阿妈','age':18,'sex':'男'}

#(1)遍历字典的key   获取的字典中所有key值， key是一个变量的名字 我们可以随便起
for key in person1.keys():
    print(key)

#(2)遍历字典的value 获取字典中所有的value值， value是一个变量的名字 我们可以随便起
for value in person1.values():
    print(value)

#(3)遍历字典的key和value    如果只写key或者value的话只会返回元素(带小括号)
for key,value in person1.items():
    print(key,value)

#(4)遍历字典的元素
for item in person.items():
    print(item)