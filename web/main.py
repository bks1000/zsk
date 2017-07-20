# coding:utf8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

import os,sys

from tornado.escape import json_decode,json_encode
from tornado.options import define, options

#添加路径
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+"\\common")
sys.path.append(os.getcwd()+"\\dbhelper")
#for p in sys.path:
#    print p,'\r\n'

import t_url as route_url

define('port', default=8000, help='run on the given port', type=int)

if __name__ == '__main__':

    #tornado.options.parse_command_line()

    #template_path参数告诉Tornado在哪里寻找模板文件
    app = tornado.web.Application(handlers=route_url.url,\
    template_path=os.path.join(os.path.dirname(__file__), "view"),\
    static_path = os.path.join(os.path.dirname(__file__),'view/static'),\
	debug = True,
    cookie_secret='jabtty')

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start() #debug = True就包括自动加载
    #instance = tornado.ioloop.IOLoop.instance()
    #自动加载
    #tornado.autoreload.start(instance)
    #instance.start()
