#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import json
#html解析,不要用正则表达式，复杂而且易错
import bs4


response = requests.get("https://www.baidu.com")
response.encoding = "utf-8"
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)

soup = bs4.BeautifulSoup(response.text)

'''
print('\n---------------------\n')
response = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response.text)

print('\n---------------------\n')
data = {
    "name": "zhaofan",
    "age": 22
}
response = requests.get("http://httpbin.org/get", params=data)
print(response.url)
print(response.text)

print('\n---------------------\n')
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print('\n---------------------\n')
print(response.json())
print('\n---------------------\n')
print(json.loads(response.text))
print('\n---------------------\n')
print(type(response.json()))

print('\n---------------------\n')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
response = requests.get("https://www.zhihu.com", headers=headers)
print(response.text)

print('\n---------------------\n')

data = {
    "name":"zhaofan",
    "age":23
}
response = requests.post("http://httpbin.org/post",data=data)
print(response.text)

print('\n---------------------\n')
files = {"files": open("./out/one_num.txt", "rb")}
response = requests.post("http://httpbin.org/post", files=files)
print(response.text)


print('\n---------------------\n')

response = requests.get("http://www.baidu.com")
print(response.cookies)

for key, value in response.cookies.items():
    print(key + "=" + value)
print('\n---------------------\n')
#正确的做法
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)

#错误的做法
requests.get("http://httpbin.org/cookies/set/number/123456")
response = requests.get("http://httpbin.org/cookies")
print(response.text)

print('\n---------------------\n')
response = requests.get("https://www.12306.cn")
print(response.status_code)

print('\n---------------------\n')
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn",verify=False)
response.encoding = "utf-8"
print(response.status_code)
print(response.text)

print('\n---------------------\n')
proxies= {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}


response  = requests.get("https://www.baidu.com",proxies=proxies)
print(response.text)
'''

