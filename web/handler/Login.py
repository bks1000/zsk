# coding:utf8

from BaseHandler import BaseHandler

import sys
sys.path.append('../')

from web.common.jsonhelper import *

class LoginHandler(BaseHandler):
    
    def __init__(self, *args, **kwargs):
        super(LoginHandler,self).__init__(*args, **kwargs)

    """
    登录控制
    """
    def get(self):
        #self.render('../view/login.html')
        self.render('login.html', page_title='登录', header_text='登录')

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
                self.set_secure_cookie('user_id',uname) #默认30天的过期时间
                self.render("index.html", page_title='主页', header_text='主页')
            else:
                msg = {'code':-1,"msg":'用户名或密码不正确！'}
                self.write(dump(msg))

