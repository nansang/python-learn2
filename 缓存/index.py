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
http://www.cnblogs.com/wupeiqi/articles/5132791.html

Memcache 是一个高性能的分布式内存对象缓存系统，用于动态web应用以减轻数据库负载。
它通过在内存中缓存数据和对象来减少数据库的次数，从而提高动态，数据库驱动网站的速度。
基于一个存储键/值对的hashmap.
其守护进程(daemon)是用c写的，但是客户端可以用任何语来编写，并通过memcached协议与守护进行通信。

天生支持集群
python-memcached模块原生支持集群操作，其原理是在内存维护一个主机列表，且集群上主机的权重值
和主机在列表中重复出现的次数成正比

一般使用目的是，通过缓存数据库查询结果，减少数据库访问次数，以提高动态web应用的速度，提高可扩展性。

那他是怎么和数据库系统关联起来的呢？？协同工作的呢

'''
'''
==================================
'''

'''
redis

key-value存储系统。和memcached类似，支持存储的value类型更多。
包括string,list,set,zset,has。
这些数据类型都支持push/pop, add/remove及取交集并集和并集及更丰富的操作。
这些操作都是原子性的。//什么是原子性？？
在这些基础上，redis支持各种不同方式的排序。
和memcached一样，数据都是缓存在内存中。
他们两都的区别在于redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，
并在此基础上实现了master-slave(主从）同步。//主从特么又是什么玩意。

api使用：
redis-py的api的使用可以分类为：
1。连接方式
2。连接池
3。操作
    string 操作
    hash 操作
    list 操作
    set 操作
    sort set 操作
4。管道
5。发布订阅

'''

'''
===========================

SQLAlchemy是python编程语言下的一款orm框架。
该框架建立在数据库api之上，使用关系对象映射进行数据库操作
简言之便是：
将对象转化成sql，然后使用数据API执行sql并获取执行结果。

'''


