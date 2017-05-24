# coding:utf8

from handler.ZskHandler import ZskHandler
from handler.Login import LoginHandler
from handler.RegHandler import RegHandler
from handler.IndexHandler import IndexHandler
from handler.MenuHandler import MenuHandler
from handler.ChartHandler import ChartHandler
from handler.MenuOPHandler import MenuOPHandler
from handler.ArticleHandler import ArticleHandler
from handler.CommonListHandler import CommonListHandler
from handler.CommonDetailHandler import CommonDetailHandler
from handler.FileHandler import FileHandler

"""
路由配置
"""

url=[(r'/zsk', ZskHandler),(r'/login', LoginHandler),(r'/reg',RegHandler),
(r'/index',IndexHandler),(r'/menu',MenuHandler),(r'/chart',ChartHandler),
(r"/(?P<nickname>.*)/article/details/(?P<postid>\d*)", ArticleHandler), #http://localhost:8000/wyx819/article/details/45652713中提取出，”wyx819”和”45652713”
(r"/(?P<coll>.*)/list", CommonListHandler),
(r"/(?P<coll>.*)/details/(?P<postid>.*)", CommonDetailHandler),
(r'/menuop',MenuOPHandler),
(r'/file', FileHandler)]
