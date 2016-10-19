#!/usr/bin/python3
# coding:utf-8

import pika
'''
=========消费者=============
'''
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'
))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("[x] received %r" %body)

channel.basic_consume(callback,
                      queue="hello",
                      no_ack=True)

print(' [*] waiting for messages. to exit press crtl+c')
channel.start_consuming()

