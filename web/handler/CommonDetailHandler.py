# coding:utf8

from common import viewconfig
from BaseHandler import BaseHandler
from bson import ObjectId

class CommonDetailHandler(BaseHandler):
    def get(self ,coll, postid):
        pt = self.get_argument('print',default='')
        data = self.db.find_one(coll,{'_id':ObjectId(postid)})
        if pt=='':
            self.render('coll/detail%s.html' % (viewconfig.version) ,coll=coll, id=postid ,title=data['title'],content=data['content'],isprint=0)
        else:
            self.render('coll/detail%s.html' % (viewconfig.version),coll=coll, id=postid ,title=data['title'],content=data['content'],isprint=1)