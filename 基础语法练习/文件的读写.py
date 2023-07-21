#写数据
fp = open('test.txt','a')
fp.write('hellow world I am here \n' * 5)
fp.close()

#如果文件存在 会先清空原来的数据 然后再写
#想在每一次执行之后追加数据
#如果模式变为了a 那么就会追加的操作

#读数据
fp = open('test.txt','r')
#默认情况下 read是一字节一字节的读 效率低
""" content = fp.read()
print(content) """

#readline是一行一行的读取 只能读取一行
""" content = fp.readline()
print(content) """

#readlines读取多行 返回的是列表
content = fp.readlines()
print(content)