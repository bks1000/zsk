# -*- coding: utf-8 -*-

"""
模块注释
ip          172.18.140.39
port        27017
database    test
coll        数据集(collection   表名)
doc         文档(document  行)

API    http://api.mongodb.com/python/current/tutorial.html?_ga=2.99986523.436002640.1494386151-1755936065.1492993264
API    http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.update_one
API    http://api.mongodb.com/python/current/genindex.html
"""
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class DbMongoClient(object):
    """
        MongoDB操作类
    """
    def __init__(self, ip, port, database):
        """
            初始私有变量
        """
        self.__ip = ip
        self.__port = port
        self.__database = database

    def __getdb(self):
        """
            通过MongoClient，获取数据库对象
            即，shell中的db
            私有函数
        """
        return MongoClient(self.__ip, self.__port)[self.__database]   #MongoClient(self.ip, self.port).test #这两种方法有一个管用或者都管用

##############################查询##################################

    def find_one(self, coll, condition):
        """
            根据条件获取单条数据
        """
        return self.__getdb()[coll].find_one(condition)

    def find(self, coll, condition, cols=None):
        """
            根据条件查询数据
            condition 查询条件，如果没有请输入 {}
            cols      查询结果列，如果没有输入 {}
            cols 说明：包含：1，排除：0。注意，不能同时出现包含和排除。
        """
        if cols is None:
            return self.__getdb()[coll].find(condition)
        else:
            return self.__getdb()[coll].find(condition, cols)

##############################新增##################################

    def insert_one(self, coll, doc):
        """
            插入单个文档
            coll    集合名
            doc     文档
            返回新文档的 _id
        """
        return self.__getdb()[coll].insert_one(doc).inserted_id

    def insert(self, coll, docs):
        """
            批量插入文档
            coll    集合名
            docs    文档数组
            返回新文档的 _id数组
        """
        return self.__getdb()[coll].insert_many(docs).inserted_ids

###########################索引#################################
    
    def create_index(self, coll, keys, **kwargs):
        """
            创建索引
            好处：避免全文扫描，提高查询效率
            坏处：影响插入效率
            慎重添加索引，索引够用就好，不要滥用。
            API:    http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.create_index
            coll    集合
            kwargs    不定参数字典，包含添加索引的列的列表和其他参数
        """
        #self.getdb()[coll].create_index(keys, **kwargs)
        self.__getdb()[coll].ensure_index(keys, **kwargs)

    def drop_index(self, coll, index_or_name):
        """
            删除索引:
            通过命令行执行 >db.user.find({'username':'june'}).explain()找到索引名

            index_or_name: index (or name of index) to drop
        """
        self.__getdb()[coll].drop_index(index_or_name)
    def index_info(self, coll):
        """
            获取有关此集合索引的信息。返回结果为字典
        """
        self.__getdb()[coll].index_information()

##############################更新##################################

    def update_one(self, coll, condition, doc):
        """
            根据条件更新单个文档
            coll        集合
            condition    条件
            doc         文档  $set 在没有字段时，添加字段，有就更新
        """
        return self.__getdb()[coll].update_one(condition, doc).matched_count


    def update(self, coll, condition, doc):
        """
            根据条件批量更新文档
            coll        集合
            condition   条件
            doc         文档
        """
        return self.__getdb()[coll].update_many(condition, doc).matched_count

##############################删除##################################

    def delete_one(self, coll, condition):
        """
            根据条件删除单个文档
            coll        集合
            condition   条件
        """
        return self.__getdb()[coll].delete_one(condition).deleted_count

    def delete(self, coll, condition):
        """
            根据条件批量删除
            coll    集合
            condition  条件
        """
        return self.__getdb()[coll].delete_many(condition).deleted_count

##################################find & op####################################

    def find_one_and_delete(self, coll, condition, sort=None):
        """
            查找并删除，多文档可以排序
            Finds a single document and deletes it, returning the document.
        """
        return self.__getdb()[coll].find_one_and_delete(condition, sort=sort)

    def find_one_and_replace(self, coll, condition, replacement,\
     sort=None, return_document=pymongo.ReturnDocument.BEFORE):
        """
            查找并替换，多文档可以排序
            Finds a single document and replaces it,\
             returning either the original or the replaced document.
             condition      查找条件
             replacement    替换文档内容
        """
        return self.__getdb()[coll].find_one_and_replace(\
        condition, replacement, sort=sort, return_document=return_document)

    def find_one_and_update(self, coll, condition, updatement,\
    sort=None, return_document=pymongo.ReturnDocument.BEFORE):
        """
            查找单个文档并更新
        Finds a single document and updates it,\
         returning either the original or the updated document.
            condition      查找条件
            updatement     更新文档内容
        """
        return self.__getdb()[coll].find_one_and_update(\
        condition, updatement, sort=sort, return_document=return_document)
##############################测试##################################


if __name__ == "__main__":
    client = DbMongoClient("172.18.140.39", 27017, "test")
    #db = client.getdb()
    #print db['log'].find()  #可行
    #print db.log.find()     #可行
    #print client.find_one("log",{"num":990});   #查询单条
    #coll = client.find("log", {"num":989}, {'_id':1,'num':1});#查询单条
    #可行
    """
    coll = client.find("log",{"num":{'$gt':995}},{'_id':1,'num':1}).sort("num", pymongo.DESCENDING);#查询num大于995的文档，倒序排列
    for doc in coll:
        print "%s \r\n _id:%s\r\n Time:%s \r\n" %(doc, doc['_id'], ObjectId(doc['_id']))
    """
    #可行
    #id = client.insert_one('user',{'username':'betty','country':"China",'age':18})
    #print id

    #可行
    """
    users = [{"username":"白开水",'age':18,'sex':'男'},
    {'username':'冰淇凌','age':18,'sex':'女'}]
    print client.insert('user',users)
    """

    #print client.find("user",{},{}).count() #查询行数
    #增加身高
    #print client.update_one("user",{ "_id" : ObjectId("590299b275b6a61d3cd6ddc3")},{'$set':{'height':179}})

    
    #print client.update("user", {"username":"june"}, {'$set':{'height':180}})
    
    #创建索引
    #client.create_index("user", 'username')  #在username上创建升序索引

    #删除索引
    #client.drop_index('user', 'username_1')

    #print client.index_info("user") #貌似没用
    #print client.delete_one('user',{"_id":ObjectId("5902a6236870df1764b0cad6")})
    
    #print client.find_one_and_delete('user',{"username" : "jones"},[('_id',pymongo.DESCENDING)])

    #将find_one_and_delete返回的文档直接拷贝到这里，然后重新插入
    #user={u'username': u'jones', u'country': u'China', u'_id': ObjectId('590042ddc0125889f173d1ba'), u'favorites': {u'movies': [u'HuoYingRenZhe', u'HaiZeiWang', u'HuoYing']}, u'height': 199}
    #client.insert_one('user',user)

    #查找并替换
    #user={'username':'白开水', 'job':'programmer', 'like':'programming'}
    #print client.find_one_and_replace("user", {'username':'白开水'}, user)

    #查找并更新
    #user ={'$set':{'sex':'man'}}
    #print client.find_one_and_update('user', {'username':'白开水'}, user)
    
    #以数组形式打印结果
    from bson import json_util as jsonb
    zsk = client.find("zsk", {})    #直接输出是：<pymongo.cursor.Cursor object at 0x0000000003E25C88>
    print jsonb.dumps(zsk)


