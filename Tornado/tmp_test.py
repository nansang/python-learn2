#!/usr/bin/python3
# coding:utf-8

'''
tornado中的模板语言和django中类似，模板引擎将模板文件载入内存，然后将数据嵌入其中，
最终获取到一个完整的字符串，再将字符串返回请求者。

tornado的模板支持"控制语句"和"表达语句"，控制语句是使用{%和%}包起来，如{% if len(items) > 2 %}.
表达语句是使用{{和}}包起来，如{{item(0) }}.

控制语句和对应的python语句的格式基本完全相同。我们支持if, for, while和try，
这些语句逻辑结果的位置需要用{% end %}做标记。
还通过extends 和 block语句实现了模板继承。这些在template模板的代码文档有详细描述。

'''

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


settings = {
    'template_path': 'home2',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

'''
模板有点问题，没有弄明白，明天：实用功能，扩展功能，我一直想写习的东东。
'''