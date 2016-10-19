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
Flask
基于python开发并且依赖jinja2模板和werkzeug wsgi服务的一个微型框架
对于werkzeug本质是socket服务端，其用于接收http请求并对请求进行预处理，然后触发flask框架
开发人员基于flask框架提供的功能对请求进行相应的处理，并返回给用户，如果要返回给用户复杂的内容中时，
需要借助jinja2模板来实现对模板的处理。

将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器

保持核心简单而易于扩展

不包含数据库抽象层，表单验证，或者其它任何中已有多种库可以胜任的功能。但是支持扩展。
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()