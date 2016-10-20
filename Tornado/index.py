#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Description:
Help:
1.http://www.tornadoweb.cn/documentation/#_4
2.http://www.cnblogs.com/wupeiqi/articles/5341480.html
'''
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hellow world!")

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()