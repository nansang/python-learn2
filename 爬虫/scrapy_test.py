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
scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。其可以应用在数据挖掘，
信息处理或存储历史数据等一系列的程序中。
其最初是为了页面抓取所设计的，也可以应用在获取api所返回的数据或者通用的网络爬虫。
scrapy用于数据挖掘，监测和自动化测试

twisted异步网络库来处理网络通讯  queuelib

主要包括以下组件：
1。引擎（scrapy) 用来处理整个系统的数据流处理，触发事务（框架核心）
2。调度器（scheduler)
3。下载器(downloader)
4。爬虫(spilders)
5。项目管道(pipeline)
6。下载器中间件(downloader middlewares)
7。爬虫中间件(spilder middlewares)
8。调度中间件(scheduler middlewares)
'''

'''
运行流程大概如此：
1.引擎从调度器中取出一个链接(url)用于接下来的抓取
2.引擎把url封装成一个请求(request)传给下载器
3.下载器把资源下载下来，并封装成应答包（response)
4.爬虫解析response
5.解析出实体(item)，交给实体管道进行进一步的处理
6.解析出的是链接(url),就把url交给调度器等待抓取

pyOpenSSL
'''

'''
登录，验证码，ajax,多线程，分布式，服务器防爬虫
'''
