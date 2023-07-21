import requests 

url = "https://assist.org/transfer/report/26287616"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}

response = requests.get(url=url,headers=headers)

content = response.text 

print(content)