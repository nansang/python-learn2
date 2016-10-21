#!/usr/bin/python3
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help: http://www.cnblogs.com/wupeiqi/articles/5341480.html
'''

'''
实用功能
对于静态文件，可以配置静态文件的目录和前段使用时的前缀，并且tornado还支持静态文件缓存。
'''
import tornado.ioloop
import tornado.web
import hashlib

class MainHandler (tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    #静态文件缓存功能，也不写全一点
    def get_content_version(cls, abspath):
        '''
        :return a version string for the resource at the given path.

        :param cls:
        :param abspath:
        :return:
        '''
        data = cls.get_content(abspath)
        hasher = hashlib.md5()


#字典么？后面为什么还有逗号？
settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8001)#为什么80不行呢
    tornado.ioloop.IOLoop.instance().start()

'''
csrf

tornado中的跨站请求伪造和django中的相似，跨站伪造请求(cross-site request forgery)
ajax使用时，本质上就是去获取本地的cookie，携带cookie再来发送请求

cookie
tornado中可以对cookie进行操作，并且还可以对cookie进行签名以方置伪造

签名
cookie很容易被恶意的客户端伪造。
加入你想在cookie中保存当前登录用户的id之类的信息，你需要对cookie作签名以防止伪造。
tornado通过set_secure_cookie和get_secure_cookie方法直接了这种功能。
要使用这些方法，你需要在创建应用时提供一个密钥，名字为cookie_secret.
你可以把它作为一个关键词参数传入应用的设置中。

签名cookie的本质
写cookie过程：
1。将值进行base64加密
2。对除值以外的内容进行签名，哈希算法（无法逆向解析）
3。拼接 签名 ＋ 加密值

读cookie过程：
1。读取 签名 ＋ 加密值
2。对签名进行验证
3。base64解密，获取值内容

许多api验证机制和安全cookie的实现机制相同，settings中设置cookie_secret
'''

