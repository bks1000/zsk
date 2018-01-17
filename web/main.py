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
    '''
    一般设置:

        autoreload: 如果设置 True,如果文件有变化进程将自动重启, 在 Debug mode and automatic reloading（DeBug模式和自动装载的情况下自动开启）.
        debug: 几种配置的集合, 具体查看 Debug mode and automatic reloading. 设置 debug=True 相当于设置 autoreload=True,compiled_template_cache=False, static_hash_cache=False, serve_traceback=True.
        default_handler_class and default_handler_args: 在页面没有找到（404错误的时候）自定义404错误页视图动作类及参数
        compress_response: 如果设置 True, responses（响应）将被自动压缩
        gzip: 在Tornado 4.0被compress_response代替
        log_function: 这个函数用来回调 RequestHandler 对象的处理结果，默认主程序导入logging并配置好的话会自动记录.也可以定制Application.log_request这个方法.
        serve_traceback: 如果设置 true,错误页面将包含错误跟踪
        ui_modules and ui_methods: 配置 UIModule 或 UI methods配置模版可用的帮助方法. 可以是一个模块、字典或一个模块或者字典的列表. 更多细节查看 UI modules
        认证和安全设置:

        cookie_secret: 被 RequestHandler.get_secure_cookie和set_secure_cookie用来配置cookie的标志
        key_version: 被 set_secure_cookie 用来配置cookie的标志时cookie_secret的一个key
        login_url: 如果没有用户登录这个 authenticated 装饰器将被重新定义到. 可以进一步重写 RequestHandler.get_login_url
        xsrf_cookies: If true, Cross-site request forgery protection will be enabled.
        xsrf_cookie_version: Controls the version of new XSRF cookies produced by this server. Should generally be left at the default (which will always be the highest supported version), but may be set to a lower value temporarily during version transitions. New in Tornado 3.2.2, which introduced XSRF cookie version 2.
        xsrf_cookie_kwargs: May be set to a dictionary of additional arguments to be passed toRequestHandler.set_cookie for the XSRF cookie.
        twitter_consumer_key, twitter_consumer_secret, friendfeed_consumer_key,friendfeed_consumer_secret, google_consumer_key, google_consumer_secret, facebook_api_key,facebook_secret: Used in the tornado.auth module to authenticate to various APIs.
        模版设置:

        autoescape: 制对模板的自动转义. 可以被设置为 None 以禁止转义, 或设置为一个所有输出都该传递过数 name . 默认是 "xhtml_escape". 可以在每个模板中改变使用 {% autoescape %} 指令.
        compiled_template_cache:  默认 True; 如果 False 每次请求将重新加载模版
        template_path: 模版文件目录. 可以被 RequestHandler.get_template_path获取进行重写
        template_loader: 分配一个 tornado.template.BaseLoader进行模版加载.如果设置了template_path和 autoescape将失效. 可以被 RequestHandler.create_template_loader进一步重写.
        template_whitespace: 对于模板中的空白处理; 详细用法请看tornado.template.filter_whitespace
        静态文件设置:

        static_hash_cache: 默认 True; 如果 False 静态 urls 将重新加载静态文件
        static_path: 静态文件的目录
        static_url_prefix: 静态文件的Url前缀, 默认为 "/static/".
        static_handler_class, static_handler_args: 可以自定义处理静态文件的动作和参数，而不是默认的 tornado.web.StaticFileHandler. static_handler_args, 如果设置了，应该有一个字典被传入到动作类的 initialize 方法中
    '''
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
