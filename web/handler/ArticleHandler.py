# coding:utf8

from BaseHandler import BaseHandler

class ArticleHandler(BaseHandler):

    def get(self, nickname, postid):
        """
        nickname 登录人昵称
        postid  文章ID
        路由映射：http://www.cnblogs.com/adc8868/p/6868391.html
        """
        self.write(nickname)
        self.write(postid)
        

    def post(self):
        pass