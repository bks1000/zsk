部署linux mongodb

修改数据库配置：web/common/dbconfig.py

使用方法：$ python main.py

以2结尾的，表示使用Vue+Elementui 


tonado在线教程：http://demo.pythoner.com/itt2zh/index.html
回头弄到知识库里。


请问如何处理tornado模板和angular.js的 {{ }} 表达式冲突问题？ 
https://www.zhihu.com/question/21324465
正解：{{! name }} 。{{! }}内的变量或表达式，不会经过tonado模板处理
    {{}}内的变量或表达式，会经过tonado模板处理


 tornado处理post请求的json数据
 http://blog.csdn.net/u010526125/article/details/70849266
 tornado只实现了格式为formdata以及urlencode两种方式的post数据的自动解析
    if("application/json" in self.request.headers["Accept"]): #根据请求头，获取传入参数
        data = self.request.body.decode('utf-8')
        param = load(data)
        _id = param["_id"];
        pid = param["pid"];
        name = param["name"];
        url = param["url"];
    else:
        _id = self.get_argument('_id', default='')
        pid = self.get_argument('pid', default='')
        name = self.get_argument('name', default='')
        url = self.get_argument('url', default='')
 
