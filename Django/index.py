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

在使用model和form时，都需要对字段进行定义并指定类型，通过modelform可以省去from中字段的定义

'''
########################################

'''
model经常性操作
1。创建数据库，设计表结构和字段
2。使用mysqldb来连接数据库，并编写数据库访问层代码
3。业务逻辑层去调用数据访问层执行数据库操作

关系对象映射

'''

################ 中间件 #################

'''
django中的中间件(middleware),在django中，中间件其实就是一个类，在请求到来和结束后，
django会根据自己的规则在合适的时机执行中间件中相应的方法。

在django项目的settings模块中，有一个MIDDLEWARE_CLASSES变量，其中每个元素就是一个中间件。

中间件有什么用么？？

'''

############### admin ###############
'''
django admin是django提供的一个后管理页面，管理页面提供完善的html和css，使得你在通过model创建完数据库表之后，
就可以对数据进行增删改查，而使用django admin以下操作：
1。创建后台管理员
2。配置url
3。注册和配置django admin后台管理页面
'''