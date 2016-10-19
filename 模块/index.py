#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help:
'''

'''
模块paramiko,用于做远程控制的模块，使用该模块可以对远程服务器进行命令或文件操作，值得一说的是,
fabric和ansible内部的远程管理就是使用的paramiko来实现。


hashlib:加密模块
json,pickle：序列列模块
configParser：特定的配置操作
logging：日志模块
datetime,time：时间模块
re：正则表达式模块
random：验证码，随机字符实现

各种模块的使用

with看起来如此简单，但是其背后还有一些工作要做，因为你不能对Python的任意符号使用with语句，
它仅能工作于支持上下文管理协议（context management protocol）的对象。
也就是说，只有内建了“上下文管理”的对象可以和with一起工作，目前支持该协议的对象有：
http://www.cnblogs.com/chenny7/p/4213447.html


打印功能字符串拼接的写法
1。最原始的字符串连接方式：str1 + str2;
2。python新字府串连接语法：str1,str2;
3。奇怪的字符串方式：str1 str2
4。% 连接字符串：‘name:%s; sex: ’ % ('tom', 'male')
5。字符串列表连接：str.join(some_list)
'''
import random
checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != 1:
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)
    checkcode += str(temp)

print(checkcode)

import hashlib

data = 'lkweuoiilk'
hash = hashlib.md5(data.encode('utf8'))
myadmin = 'admin'
hash.update(myadmin.encode('utf8'))
print(hash.hexdigest())

#报错提示没有看懂
# import hmac
#
# h = hmac.new('wuqi')
# h.update('hlelow')
# print(h.hexdigest())

import pickle
data = {'k1':123, 'k2':'hello'}

#将数据通过特殊的形势转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)

str= str(data)

#写入文件，这个with是做什么来的？
with open('result.pk', 'wb') as fp:

    pickle.dump(data, fp)

import json

#所有程序语言都认识的字符串
j_str = json.dumps(data)
print(j_str)

with open('result.json', 'w') as fp:
    json.dump(data, fp)


import logging

import time
print(time.time())
print(time.mktime(time.localtime()))
print(time.gmtime())
print(time.localtime())
print(time.strptime('2014-11-11', '%Y-%m-%d'))

print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d',time.localtime())) #默认当前时间
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.ctime(time.time()))
print(time.strftime('%Y-%m-%d',time.localtime())) #默认当前时间
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.ctime(time.time()))


import datetime

print(datetime.datetime.now())
print(datetime.datetime.now() - datetime.timedelta(days=5))#这写法也太彪悍了吧

import re

obj = re.match('\d+', '123uuasf3242fs2342')
if obj:
    print(obj.group())