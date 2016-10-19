#!/usr/bin/env python3
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
众所周知 对于所有的web应用，本质上其实就是一个socket服务器，用户的浏览器其实就
是一个socket客户端
http://www.cnblogs.com/wupeiqi/articles/5237672.html


'''
import socket

# def handle_request(client):
#     buf = client.recv(1024)
#     client.send("HTTP/1.1 200 OK\r\n\r\n")
#     client.send("Hello, Seven")
#
# def main():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('localhost', 8000))
#     sock.listen(5)
#
#     while True:
#         connection, address = sock.accept()
#         handle_request(connection)
#         connection.close()

# if __name__ == '__main__':
#     main()

'''
服务器程序和应用程序
服务器程序负责对socket服务器进行封装，并在请求到来时，对请求的各种数据进行整理。
应用程序则负责逻辑处理。
为了方便应用程序的开发，就出现了众多的web框架，Django,Flask,Tornado.
不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提示服务。
我们可以设定一个标准，只要服务器程序支持这个标准，框架也支持这个标准，那么他们就可以配合使用。
之前就生成了一个标准WSGI.

python标准库提供的独立WSGI服务器称为wsgiref.
'''
'''
from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    start_response('200 OK'[('Content-Type', 'text/html')])
    return '<h1>Hello, Web!</h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print('Serving Http on port 8000...')
    httpd.serve_forever()

'''
'''
自定义Web框架
1。框架
2。模板引擎

本人估计代码有问题，可能是不支持python3的原因，先放一放
'''
from wsgiref.simple_server import make_server

def index():
    # return 'index'
    f = open('index.html')
    data = f.read()
    return data

def login():
    # return 'login'
    f = open('login.html')
    data = f.read()
    return data

def rounters():

    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )
    return urlpatterns


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    # print('url='+url)
    urlpatterns = rounters()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func
    else:
        return '404 not found'

    # return '<h1>Hello, Web!</h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print('Serving Http on port 8000...')
    httpd.serve_forever()

'''
之后研究各个框架实现的方式

WSGI（Web Server Gateway Interface）是一种规范，
它定义了使用python编写的web app与web server之间接口格式，
实现web app与web server间的解耦。

研究一下wsgi
'''
