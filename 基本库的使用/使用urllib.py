#%%
import urllib.request

response = urllib.request.urlopen("https://live.bilibili.com/")
print(response.read().decode("utf-8"))#打印该网址的源代码
print(type(response)) #<class 'http.client.HTTPResponse'>


# %%
