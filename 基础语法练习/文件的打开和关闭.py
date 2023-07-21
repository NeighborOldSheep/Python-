

#创建一个test.txt文件

# open(文件路径，访问模式)
#访问模式:  w可写  r可读
""" fp = open('test.txt','w')
fp.write('Hello World') """

#文件夹是不可以创建的   暂时需要手动创建
""" fp = open('demo/text.txt','w')
fp.write('hello shangguigu') """


#文件的关闭
fp = open('a.txt','w')
fp.write('1111')
fp.close()