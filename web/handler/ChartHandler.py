# coding:utf8

from BaseHandler import BaseHandler
from common import viewconfig

class ChartHandler(BaseHandler):

    def get(self):
        self.render("chart%s.html" % (viewconfig.version))