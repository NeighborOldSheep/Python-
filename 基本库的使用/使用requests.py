#%%
import requests

r = requests.get("https://live.bilibili.com/")
print(r.status_code)    #200
print(type(r))          #<class 'requests.models.Response'>
print(r.cookies)
print(r.text)
# %%
import requests

data = {
    "age" : 22,
    "name" : "Tom"
}

r = requests.get("https://httpbin.org/get", params = data)
print(r.text)
# %%
import requests

r = requests.get("https://httpbin.org/get")
print(type(r.text))     #<class 'str'>
print(r.json())
print(type(r.json()))   #<class 'dict'>


# %%
