#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help:http://www.cnblogs.com/wupeiqi/articles/5354900.html
'''

'''
Requests库
自动登陆抽屉并点赞
"破解"微信公众号
Scrapy
'''
#感觉这才有搞头

'''
网络爬虫，是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。
另外还有一些不常用的名字蚂蚁，自动索引，模拟程序或者蠕虫(FOAF社区）

Requests 是使用apache2 licensed许可证的基于python开发的http库，
其在python内置模块的基本上进行了高度的封装，
从而使得pythoner进行网络请求时，变得美好了许多，
使用requests可以轻而易举的完成浏览器可有的任何操作
'''

import requests

payload = {'key1':'value1', 'key2':'value2'}
ret = requests.get('http://httpbin.org/get', params=payload)

print(ret.url)
print(ret.text)
print(ret.headers)

import requests
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
headers = {'content-type':'application/json'}
ret = requests.post(url, data=json.dumps(payload), headers=headers)

print(ret.text)
print(ret.cookies)

#注意requests传的一些参数

'''
自动登录抽屉并点赞
gpsd是什么？
'''
#首先登录任何页面，获取cookie
i1 = requests.get(url="http://dig.chouti.com/help/service")

### 用户登录，携带上一次的cookie, 后台对cookie中的gpsd进行授权

i2 = requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': '86手机号',
        'password': '密码',
        'oneMonth': ''
    },
    cookies=i1.cookies.get_dict()
)

### 点赞（只需要携带已经授权的gpsd即可）

gpsd =i1.cookies.get_dict()["gpsd"]
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=8589523",
    cookies={'gpsd': gpsd}
)
print('i1:%s'%i1.cookies)
print('i2:%s'%i2.cookies)

'''
授权登录
'''