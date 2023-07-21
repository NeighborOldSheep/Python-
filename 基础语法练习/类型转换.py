#转换为整形

#str -> int
a = '123'
print(type(a)) # <class 'str'>
b = int(a)
print(type(b)) #<class 'int'>


#bollean --> int
a = True
print(type(a))
b = int(a)
print(b) # 1  如果是False就是0


#特殊字符无法转换  例如  . 字母 等
""" a = '1.23'
print(type(a))
b = int(a)
print(b) """


#浮点类型转换
a = '12.34'
print(type(a))
b = float(a)
print(b)


#转换为字符串
a = 80
print(type(a))
b= str(a)
print(b)

#Boolean类型转换为string类型
a = True
b = str(a)
print(b)    # 'True'


#整数变Boolean 除了0以外都是 True
a = -1
b = bool(a)
print(b)    # True

#字符串中有内容 在强制类型转换为Boolean时则返回true,空返回false
a = '123456'
b = bool(a)
print(b)

#列表转换Boolean; 列表有数据则返回True，空列表则False  字典元组一样
a = ['吴亦凡']
b = bool(a)
print(b)