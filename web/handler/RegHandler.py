# coding:utf8

from BaseHandler import BaseHandler
import sys
sys.path.append('../')
from dbhelper.dbmongo import DbMongoClient
from common.dbconfig import ip, port, database

from common.jsonhelper import *

class RegHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(RegHandler,self).__init__(*args, **kwargs)
    """
    注册业务处理
    """
    def get(self):
        return self.render('login%s.html' % (viewconfig.version), page_title='注册', header_text='注册')

    def post(self):
        uname = self.get_argument('username', default='')
        pwd = self.get_argument('pwd', default='')
        if uname == '':
            self.get()
        else:
            exist = self.db.find('user',{"$or":[{'username':uname}, {'email':uname}]}).count()
            if exist > 0:
                err = {"code":-1, "msg":"用户名已经被注册!"}
                self.write(dump(err))
            else:
                result = self.db.insert_one('user',{'username':uname,'email':uname,'pwd':pwd})
                if result > 0:
                    self.render("index.html", page_title='主页', header_text='主页')
                else:
                    msg = {'code':result,"msg":"注册失败!"}
                    self.write(dump(msg))
