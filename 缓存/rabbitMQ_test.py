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
RabbitMQ是一个在AMQP基础上完成的，可复用的企业消息系统。
他遵循Mozilla Public License开源协议。

MQ全称message queue,消息队列（MQ)是一种应用程序对应用程序的通讯方法。
应用程序通过读写入队列的消息（针对应用程序的数据）来通信，而无需专用连接来连接发他们。
消息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信，
直接调用通是用于诸如远程过程调用的技术。
排队指的是应用程序通过队列来通信。
队列的使用除去了接收和发送应用程序同时执行的要求。

（关键点是在不用专门连接来连接他们么？）

'''

#生成产消费者模型
'''
对于rabblitmq来说，生产和消息不再针对内存里的一个queue对象，
而是某台服务器上的rqbbitmq server实现的消息队列。
'''
import queue
import threading

message = queue.Queue(10)

def producer(i):
    while True:
        message.put(i)

def consumer(i):
    while True:
        msg = message.get()

for i in range(12):
    t = threading.Thread(target=producer, args=(i, ))
    t.start()
    print(t.name)

for i in range(10):
    t = threading.Thread(target=consumer, args=(i, ))
    t.start()
    print(t.name,t.daemon)

'''
连接－－－
'''