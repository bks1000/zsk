# coding:utf8
"""
菜单管理
"""

from BaseHandler import BaseHandler

from web.common.jsonhelper import *

class MenuHandler(BaseHandler):
    """def __init__(self, *args, **kwargs):
        super(MenuHandler, self).__init__(*args, **kwargs)"""
    
    def get(self):
        moc = self.get_argument('moc', default=''); #是左侧菜单，还是下拉框
        menus = self.db.find('menu',{})
        menus = list(menus)
        for k in menus:
            k['_id'] = str(k['_id'])
            k['id'] = str(k['_id'])
            if k.has_key('children'):
                for c in k['children']:
                    c['_id'] = str(c['_id'])
                    c['id'] = str(c['_id'])
        if moc=='':
            self.write(dump(menus))
        else:
            menus.insert(0,{'_id':"","id":"","text":"根级目录"})
            self.write(dump(menus))