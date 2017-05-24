# coding:utf8

from BaseHandler import BaseHandler
from bson import ObjectId

class CommonDetailHandler(BaseHandler):
    def get(self ,coll, postid):
        data = self.db.find_one(coll,{'_id':ObjectId(postid)})
        self.render('coll/detail.html',coll=coll, id=postid ,title=data['title'],content=data['content'])