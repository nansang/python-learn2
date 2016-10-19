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
Bottle是一个快速，简洁，轻量级的基于wsig的微型web框架，些框架只由一个.py文件，
除了python的标准库外，其不依赖于其它任何模块

大致可以分为以下部分：
1。路由系统，将不同请求交由指定函数处理
2。模板系统，将模板中的特殊语法渲染成字符串，值得一说的是bottle的模板引擎可以任意指定：
bottle内置模板，mako,jinja2,cheetah
3。公共组件，用于提借处理请求的相关信息，如：表单数据，cookies,请求头等
4。服务，bottle默认支持多种基于wsgi的服务
'''

#基本使用
from bottle import template, Bottle

root = Bottle()
@root.route('/hello/')
def index():
    return "hello world"

root.run(host='localhost', port=8080)

'''
路由系统：

'''
