# -*- coding: utf-8 -*-


from scrapy.conf import settings
from csdnzsk.DbHelper.DbMongo import DbMongoClient

class CsdnzskPipeline(object):
    
    #定义一个类方法from_settings，得到settings中的Mysql数据库配置信息，得到数据库连接池dbpool
    """@classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        dbparams = dict(
            ip=settings['MongoDB_HOST'],#读取settings中的配置
            port=settings['MongoDB_PORT'],
            database=settings['MongoDB_DBName']
        )
        db = DbMongoClient(**dbparams)
        return cls(db)#相当于db付给了这个类，self中可以得到
    """
    #__init__中会得到db对象
    def __init__(self):
        self.ip = '172.18.140.39' #通过settings获取之后报错:PyMongo + Scrapy = name must be an instance of basestring
        self.port = 27017
        self.database = 'test'
        self.db = DbMongoClient(self.ip, self.port, self.database)

    #pipeline默认调用
    def process_item(self, item, spider):
        '''
            数据存储
        '''
        self.db.insert_one("zsk", {'name' : item["name"], 'url' : item['url']})
