""" import re


# 从链接中提取数字部分
match = re.search(r'2022/(\d+)/', "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/11/1101.html")

print(match)
             """

import re

url = "http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/11/1101.html"

# 使用正则表达式匹配2022后面斜杠后面的数字
match = re.search(r'2022/(\d+)/', url)
if match:
    number_after_2022 = match.group(1)
    print(number_after_2022)
else:
    print("No match found.")