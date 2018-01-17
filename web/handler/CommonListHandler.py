# coding:utf8
from common import viewconfig
from BaseHandler import BaseHandler
from common.jsonhelper import *
from bson import ObjectId

class CommonListHandler(BaseHandler):
    def get(self, coll):
        id = self.get_argument('id', default='') #返回数据
        act = self.get_argument('act', default='') #返回页面
        if id == '' and act == '':
            self.render("coll/list%s.html" % (viewconfig.version),coll=coll)
        elif id == 'all':
            #查询全部
            datas = self.db.find(coll,{},{'content':0}) #不包含文档中的content字段
            datas = list(datas)
            for data in datas:
                data['_id'] = str(data['_id'])
                data['id'] = data['_id']
            self.write(dump(datas))
        elif len(id)>0 and act == '':
            #查询单个
            datas = self.db.find_one(coll,{'_id':ObjectId(id)})
            datas['_id'] = str(datas['_id'])
            datas['id'] = datas['_id']
            self.write(dump(datas))
        elif act == 'add':
            #返回新增页面
            self.render("coll/add%s.html" % (viewconfig.version),coll=coll,title='',stars='',conent='',_id='')
        elif act == 'edit':
            #返回修改页面
            self.render("coll/add%s.html" % (viewconfig.version),coll=coll,title='',stars='',conent='',_id=id)
        elif act == 'del':
            self.db.delete_one(coll,{"_id":ObjectId(id)})
            self.write("删除成功！")

    def post(self,coll):
        _id=''
        title=''
        stars=''
        content=''
        try:
            if("application/json" in self.request.headers["Accept"]):
                data = self.request.body.decode('utf-8')
                param = load(data)
                _id = param["_id"];
                title = param["title"];
                stars = param["stars"];
                content = param["content"];
            else:
                title = self.get_argument('title', default='')
                stars = self.get_argument('stars', default='')
                _id = self.get_argument('_id', default='')
                content = self.get_argument('content', default='')
        except :
            pass
        
        if _id == '':
            #新增
            self.db.insert_one(coll,{'title':title, 'stars':stars, 'content':content})
        else:
            #修改
            self.db.find_one_and_update(coll,{'_id':ObjectId(_id)},{'$set':{'title':title, 'stars':stars, 'content':content}})

        self.write("保存成功")
