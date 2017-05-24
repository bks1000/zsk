# coding:utf8

from BaseHandler import BaseHandler
from web.common.jsonhelper import *
from web.common.authenticated import authenticated


class IndexHandler(BaseHandler):

    @authenticated
    def get(self):
        self.render("index.html",page_title='主页', header_text='主页');

    def post(self):
        """
        登录
        """
        uname = self.get_argument('username', default='')
        pwd = self.get_argument('pwd', default='')
        if uname == '':
            self.get()
        else:
            exist = self.db.find('user',{"$or":[{'username':uname}, {'email':uname}],"$and":[{'pwd':pwd}]}).count()
            if exist >0:
                print 'login success'
                self.render("index.html", page_title='主页', header_text='主页')
            else:
                msg = {'code':-1,"msg":'用户名或密码不正确！'}
                self.write(dump(msg))
        