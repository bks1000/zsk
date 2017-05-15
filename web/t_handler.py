# coding:utf8
import pymongo
from tornado.web import RequestHandler
from DbHelper.DbMongo import DbMongoClient 

from jsonhelper import JSONEncoder
from bson import json_util as jsonb
from bson import ObjectId

#解决js跨域请求问题
class BaseHandler(RequestHandler):
    """
        所有Handle的基类
    """

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


# python hello.py
# http://localhost:8000/
# http://localhost:8000/?greeting=june
class IndexHandler(BaseHandler):   
    def get(self):   
        greeting = self.get_argument('greeting', 'Hello')   
        self.write(greeting + ', friendly user!')

# http://localhost:8000/zsk
# 使用EASYUI访问
class ZskHandler(BaseHandler):
    """
        知识库操作
    """
    def __init__(self, *args, **kwargs):
        #BaseHandler.__init__(self)
        super(ZskHandler, self).__init__(*args, **kwargs)
        #通过settings获取之后报错:PyMongo + Scrapy = name must be an instance of basestring
        ip = '172.18.140.39'
        port = 27017
        database = 'test'
        self.db = DbMongoClient(ip, port, database)

    def get(self):
        #self.write(jsonb.dumps(db.find("zsk", {})))

        zsk = self.db.find("zsk", {}).sort("stars",pymongo.DESCENDING) #返回的是一个游标(pymongo.cursor.cursor)，意味着循环遍历一次以后，游标指向末尾
        print zsk.count()
        zsk = list(zsk)         #将查询结果转list类型
        #循环将_id 从ObjectId类型转为string类型
        for k in zsk:
            k['_id'] = str(k['_id'])
        self.write(jsonb.dumps(zsk))

    def post(self, *args, **kwargs):
        """
            处理post请求，为ID设置星级
        """
        #print '*',args,len(args)
        #print '**',kwargs
        _id = self.get_argument('_id')
        score = self.get_argument('score')
        self.db.update_one('zsk',{'_id':ObjectId(_id)},{'$set':{'stars':score}})
        self.write(u'0')

        