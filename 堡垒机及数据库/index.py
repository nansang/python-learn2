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
开发堡垒机之前，先来学习python的paramiko模块，该模块基于ssh用于连接远程服务器并执行相关操作

'''
import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
'''
然后paramiko导入的有点问题
'''

'''
保垒机的实现：http://www.cnblogs.com/wupeiqi/articles/5095821.html

执行流程
1。管理员为用户在服务器上创建账号（将公钥放置服务器，或者使用用户名密码）
2。用户登陆堡垒机，输入堡垒机用户名密码，显示当前用户管理的服务器列表
3。用户选择服务器，并自动登陆
4。执行操作并同时将用户操作记录

'''
import getpass

user = raw_input('username:')
pwd = getpass.getpass('password')
if user == 'alex' and pwd == '123':
    print('登录成功')
else:
    print('登录失败')

'''
1。打开一个通道
2。获取一个终道
3。激活器

后面的看那个开源堡垒机
jumpserver:

https://github.com/jumpserver/jumpserver
'''



