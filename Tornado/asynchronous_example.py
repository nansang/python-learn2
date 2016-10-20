#!/usr/bin/env python3
# coding:utf-8

'''
异步非阻塞实例
'''
import tornado.ioloop
import tornado.web
from tornado import httpclient
from tornado.web import asynchronous
from tornado import gen

import uimodules as md
import uimethods as mt

class MainHandler(tornado.web.RequestHandler):
    @asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        print('start get ')
        http = httpclient.AsyncHTTPClient()
        http.fetch("http://127.0.0.1:8008/post/", self.callback)
        self.write('end respone')

    def callback(self, response):
        print(response.body)

settings = {

    'template_path': 'home',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'ui_methods': mt,
    'ui_modules': md,

}

application = tornado.web.Application([

    (r"/index", MainHandler),

], **settings)

if __name__ == "__main__":

    application.listen(8009)
    tornado.ioloop.IOLoop.instance().start()
