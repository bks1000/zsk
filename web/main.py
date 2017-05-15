# coding:utf8
import tornado.httpserver   
import tornado.ioloop   
import tornado.options   
import tornado.web 

from tornado.escape import json_decode,json_encode  
from tornado.options import define, options  

import t_url

define('port', default=8000, help='run on the given port', type=int)



if __name__ == '__main__':
    #tornado.options.parse_command_line()   
    app = tornado.web.Application(handlers=t_url.url)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
