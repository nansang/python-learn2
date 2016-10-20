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
Python的WEB框架有django, tornado, flask等多种，django相较与其它web框架其优势：
大而全
框架本身集成了orm，模型绑定，模板引擎，缓存，session等诸多功能。

终端命令：django-admin startproject sitename
ide创建django程序时，本质上都是自动执行上述命令

'''
############# 配置文件 ############settings.py

'''
    数据库
    DATABASES
    由于django内部连接mysql时使用的是mysqldb模块，而python3中还无此模板，所以
    需要pymysql来代替
    如下设置放置的与project同名的配置的__init__.py文件中
    import pymysql
    pymysql.install_as_MySQLdb()

    模板
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR,'templates'),
    )

    静态文件
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static'),
    )

'''

############# 路由系统 ################

'''
1。每个路由规则对应一个view中的函数
2。根据app对路由规则进行一次分类

django中的路由系统和其他语言的框架有所不同，在django中每一个请求的url都要有一条路由映射，
这样才能将请求交给一个view中的函数去处理。
其他大部分的web框架则是对一类的url请求做一条路由映射，从而路由系统变得简洁。
'''

'''
今天先这样

模板 form model 中间件 admin 跨点请求伪造 cookie session 分页 缓存 序列化 信号

'''