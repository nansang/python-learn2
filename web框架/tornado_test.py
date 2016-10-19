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
tornado
是friendfeed使用的可扩展的非阻塞式web服务器及其相关工具的开源版本
非阻塞式服务器，而且速度相当快。得得于其它非阻塞的方式和对epoll的运用，对于实时web服务很友好

'''
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

'''
http://www.cnblogs.com/wupeiqi/articles/5341480.html

现在的情况是：如何支持多种wsgi标准
'''
