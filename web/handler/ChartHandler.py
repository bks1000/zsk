# coding:utf8

from BaseHandler import BaseHandler

class ChartHandler(BaseHandler):

    def get(self):
        self.render("chart.html")