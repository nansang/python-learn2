#!/usr/bin/python3
# coding:utf-8

'''
session实现机制

一致性哈希
http://www.cnblogs.com/wupeiqi/articles/5341480.html
'''

import tornado.ioloop
import tornado.web
from hashlib import sha1
import os, time

session_container = {}

from hashlib import sha1
import os, time

create_session_id = lambda: sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()


class Session(object):
    session_id = "__sessionId__"

    def __init__(self, request):
        session_value = request.get_cookie(Session.session_id)
        if not session_value:
            self._id = create_session_id()
        else:
            self._id = session_value
        request.set_cookie(Session.session_id, self._id)

    # def __getitem__(self, key):

    # 根据 self._id ，在一致性哈西中找到其对应的服务器IP
    # 找到相对应的redis服务器，如： r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # 使用python redis api 链接
    # 获取数据，即：
    # return self._redis.hget(self._id, name)

    # def __setitem__(self, key, value):

    # 根据 self._id ，在一致性哈西中找到其对应的服务器IP
    # 使用python redis api 链接
    # 设置session
    # self._redis.hset(self._id, name, value)


    # def __delitem__(self, key):
        # 根据 self._id 找到相对应的redis服务器
        # 使用python redis api 链接
        # 删除，即：
        # return self._redis.hdel(self._id, name)


# Session