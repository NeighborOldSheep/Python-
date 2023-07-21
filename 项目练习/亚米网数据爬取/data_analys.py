import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 加载中文字体
font = FontProperties(fname='ZiYuYongSongTi-2.ttf', size=14)

fig, ax = plt.subplots(figsize=(10, 6))

# 读取数据
data = pd.read_excel('data.xlsx',nrows=5)

# 绘制条形图
plt.bar(data['Name'], data['Sale'])
plt.xlabel('商品名称', fontproperties=font)
plt.ylabel('销量', fontproperties=font)
plt.title('商品销量', fontproperties=font)
plt.show()