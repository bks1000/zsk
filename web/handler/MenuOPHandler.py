# coding:utf8

from BaseHandler import BaseHandler
from common import viewconfig

#import sys
#sys.path.append('../')
from dbhelper.dbmongo import DbMongoClient
from common.dbconfig import ip, port, database
from common.jsonhelper import *
from bson import ObjectId

class MenuOPHandler(BaseHandler):

    def get(self):
        d = self.get_argument('data', default='')
        act = self.get_argument('act', default='') #操作
        if d == '' and act == '':
            self.render("menu/index%s.html" % (viewconfig.version))
        elif d != '' and act == '':
            #查询菜单表数据，返回JSON
            menus = list(self.db.find('menu', {}))
            for k in menus:
                k['_id'] = str(k['_id'])
                k['id'] = k['_id']
                if k.has_key('children'):
                    for c in k['children']:
                        c['_id'] = str(c['_id'])
                        c['id'] = str(c['_id'])
            self.write(dump(menus))
        elif act != '':
            if act == 'add':
                self.render('menu/add%s.html' % (viewconfig.version),_id='',pid='')
            elif act == 'update':
                _id = self.get_argument("_id")
                pid = self.get_argument("pid", default='')
                self.render('menu/add%s.html'% (viewconfig.version), _id=_id, pid=pid)
            elif act == 'find':
                _id = self.get_argument("_id")
                data = self.db.find('menu', {'_id':ObjectId(_id)}, {'children':0})
                data = list(data)
                if len(data) > 0:
                    #主节点
                    data = data[0]
                    data['_id'] = str(data['_id'])
                    self.write(dump(data))
                else:
                    #子节点
                    data = self.db.find('menu', {"children":{'$elemMatch':{"_id":ObjectId(_id)}}})
                    lst = list(data)[0]['children']
                    dd = None
                    for dic in lst:
                        if dic['_id'] == ObjectId(_id):
                            dic['_id'] = str(dic['_id'])
                            dd = dic
                            break
                    self.write(dump(dd))

    def post(self):
        act = self.get_argument('act', default='') #操作
        _id=''
        pid=''
        name=''
        url=''

        #tornado只实现了格式为formdata以及urlencode两种方式的post数据的自动解析
        #判断传入参数方式，根据不同方式，用不同方法解析参数。
        try:
            if("application/json" in self.request.headers["Accept"]):
                data = self.request.body.decode('utf-8')
                param = load(data)
                _id = param["_id"];
                pid = param["pid"];
                name = param["name"];
                url = param["url"];
            else:
                _id = self.get_argument('_id', default='')
                pid = self.get_argument('pid', default='')
                name = self.get_argument('name', default='')
                url = self.get_argument('url', default='')
        except :
            pass
        
        
        if act == 'save':
            result = ''
            if _id == '':
                #新增
                if pid == '':
                    result = self.db.insert_one('menu', {'text':name, 'pid':pid, 'attributes':{'url':url}})
                else:
                    result = self.db.update_one('menu', {'_id':ObjectId(pid)}, \
                    {'$push':{"children":{'_id':ObjectId(), 'text': name, 'pid':pid, 'attributes': {'url':url}}}})
                    """删除嵌入文档
                    db.collection.update(
                        { _id: ObjectId('id') },
                        { $pull: { links: { name: 'Baidu' } } }
                    );
                    """
            else:
                data = self.db.find('menu', {'_id':ObjectId(_id)})
                if len(list(data)) > 0:
                    #主节点
                    result = self.db.find_one_and_update('menu',{'_id':ObjectId(_id)},\
                    {'$set':{'text':name,'attributes.url':url,'pid':pid}})
                else:
                    #子节点更新
                    #通过文档的_id和文档的children字段的_id字段，找到要更新的内嵌文档，然后更新内嵌文档字段
                    #注意写法！！
                    result = self.db.update('menu', {"_id":(ObjectId(pid)), 'children._id':(ObjectId(_id))},\
                    {'$set':{'children.$.text':name,'children.$.attributes.url':url,'children.$.pid':pid}})

        elif act == 'del':
            count = self.db.delete_one("menu", {'_id':ObjectId(_id)})
            if count == 0:
                self.db.update('menu',
                    { '_id': ObjectId(pid) },
                    { '$pull': {'children':{'_id': ObjectId(_id) }}}
                );
                    

        self.write(dump({'code':1}))
