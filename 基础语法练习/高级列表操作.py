#列表添加

#append()方法  会添加到列表末尾

food = ['铁锅炖大额','酸菜五花肉']
food.append('锅包肉')
print(food)


#insert()方法  insert(index,object) 插入指定的索引
name = ['a','c','d']
name.insert(1,'b')
print(name)

#extend() 里面的数据必须是可以迭代的(很多数据) 将另一个列表中的元素拼接到另一个列表当中
num_list = [1,2,3]
num1_list=[4,5,6]

num_list.extend(num1_list)
print(num_list)



#列表修改
city_list = ['Alhambra',"Monetarypark",'DimondBar']
print(city_list)
#可以通过下标修改
city_list[1] = 'Azusa'
print(city_list)


#列表查询  in是判断某一个元素在某一个列表中
food_list = ['锅包肉','东北乱炖','汆白肉']

#要判断在控制台输入的数据 是否在列表中
food = input('请输入您想吃的食物')
if food in food_list:
    print("在菜单里")
else:
    print('不在菜单')



#列表删除
"""  
    del: 根据下标删除
    pop: 删除最后一个元素
    remove: 根据元素的值进行删除
"""
a_list = [1,2,3,4,5,6,7,8,9]
print(a_list)

#根据下标来删除列表中的元素
del a_list[2]
print(a_list)

#删除最后一个元素
b_list = [1,2,3,4,5,6,7,8,9]
print(b_list)

b_list.pop()
print(b_list)


#根据元素来删除列表中的数据
c_list = [1,2,3,4,5,6,7,8,9]
print(c_list)

c_list.remove(3)
print(c_list)