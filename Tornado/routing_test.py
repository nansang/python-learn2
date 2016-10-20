#!/usr/bin/env python3
# coding:utf-8

'''
路由系统其实就是url和类的对应关系，这里不同于其它框架，其它很多框架均是url对应函数，
tornado中每个url对应的是一个类。
**类**
'''
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, stroy_id):
        self.write("you requested the sotry " + stroy_id)

class BuyHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("buy.wupeiqi.com/index")

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])

#这个写法是几个意思
application.add_handlers('buy.wupeiqi.com$',[
    (r'/index', BuyHandler),
])

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()



