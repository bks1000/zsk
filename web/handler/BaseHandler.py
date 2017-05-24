# coding:utf8

from tornado.web import RequestHandler

import sys
sys.path.append('../')
from web.dbhelper.dbmongo import DbMongoClient
from web.common.dbconfig import ip, port, database

#解决js跨域请求问题
class BaseHandler(RequestHandler):
    """
        所有Handle的基类
    """
    def __init__(self, *args, **kwargs):
        #BaseHandler.__init__(self)
        super(BaseHandler, self).__init__(*args, **kwargs)
        #通过settings获取之后报错:PyMongo + Scrapy = name must be an instance of basestring
        #ip = '172.18.140.39'
        #port = 27017
        #database = 'test'
        self.db = DbMongoClient(ip, port, database)

    #http://www.jb51.net/article/49792.htm
    def get_login_url(self):
        return '/login'

    def get_current_user(self):
        return self.get_secure_cookie('user_id')

    #允许跨域请求
    def set_default_headers(self):
        #self.set_header('Access-Control-Allow-Origin', '*')
        #self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        #self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', '*')
        #self.set_header('Content-type', 'application/json')
        pass

