# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
#from twisted.enterprise import adbapi 

#保存到数据库的类CsdnzskPipeline（在settings中声明）
class CsdnzskPipeline(object):
    
    #定义一个类方法from_settings，得到settings中的Mysql数据库配置信息，得到数据库连接池dbpool
    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。 
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        dbparams = dict(
            host=settings['MYSQL_HOST'],#读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#编码要加上，否则可能出现中文乱码问题
            use_unicode=False,
        )
        db = mysql.connector.connect(**dbparams) #**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(db)#相当于dbpool付给了这个类，self中可以得到
    
    #__init__中会得到连接池dbpool
    def __init__(self, db):
        self.db = db
    
    #pipeline默认调用
    def process_item(self, item, spider):
        #query=self.dbpool.runInteraction(self._conditional_insert,item)#调用插入的方法
        #query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        cursor = self.db.cursor()
        sql="insert into csdnzsk(name,url) values('%s','%s')" % (item["name"],item["url"])
        print "%s \r\n" % (sql)
        cursor.execute(sql)
        # 提交到数据库执行
        self.db.commit()
        return item

    #写入数据库中
    """def _conditional_insert(self,tx,item):
        #print item['name']
        sql="insert into csdnzsk(name,url) values(%s,%s)"
        params=(item["name"],item["url"])
        tx.execute(sql,params)"""

     #错误处理方法
    def _handle_error(self, failue, item, spider):
        print failue
