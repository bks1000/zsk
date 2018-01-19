# coding:utf8

from BaseHandler import BaseHandler
from common.jsonhelper import *
import time
import os
import json
import re

'''
ueditor(通过参考php版的ueditor而来)
文件上传下载处理类
'''

class FileHandler2(BaseHandler):

    def get(self):
        """
        action=config表示获取ueditor的配置信息，在ueditor初始化时，自动请求
        """
        action=self.get_argument('action','')
        if(action!='' and action=="config"):
            #with open(os.getcwd()+'\\web\\handler\\ueconfig.json') as json_file:
            #说明，命令行启动，不需要加web前缀
            #     调试启动，需要加web前缀，以后再研究
            with open(os.getcwd()+'\\handler\\ueconfig.json') as json_file:
                data = json.load(json_file)
                #return data
                self.write(data)
        elif (action!="" and action=='listimage'):
            pass
        else:
            '''
            文件下载
            '''
            filename = self.get_argument('filename', default='')
            if filename == '':
                self.write('')
                return
            
            #说明，命令行启动，不需要加web前缀
            #     调试启动，需要加web前缀，以后再研究
            filepath = os.getcwd();
            #filename = filepath + '\\web\\view\\static\\upload\\' + filename
            filename = filepath + '\\view\\static\\upload\\' + filename

            #self.set_header ('Content-Type', '*/*')
            #self.set_header ('Content-Disposition', 'attachment; filename=' + filename)

            #读取的模式需要根据实际情况进行修改
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    self.write(data)
            #记得有finish哦
            self.finish()

    def post(self):
        '''
        文件上传
        '''
        #文件的暂存路径
        filepath = os.getcwd();
        #说明，命令行启动，不需要加web前缀
        #     调试启动，需要加web前缀，以后再研究
        #upload_path = filepath + '\\web\\view\\static\\upload\\'
        upload_path = filepath + '\\view\\static\\upload\\'
        #upload_path=os.path.join(os.path.abspath('view/static/upload')) 
        
        #提取表单中‘name’为‘upfile’的文件元数据
        file_metas=self.request.files['upfile'][0]
        #callback = self.get_argument("CKEditorFuncNum"); 
        
        filename = str(int(time.time()))+file_metas['filename'] #添加时间戳，防止重名
        filepath=os.path.join(upload_path,filename)
        #有些文件需要已二进制的形式存储，实际中可以更改
        with open(filepath,'wb') as up:      
            up.write(file_metas['body'])
        
        url = '/file2?filename='+ filename
        result = {'original':file_metas['filename'],'state':'SUCCESS','title':filename,'url':url}
        self.write(dump(result)) #直接输出上传文件的URL地址
        #下面调用CKEDITOR的函数，为URL赋值
        #self.write("<script type=\"text/javascript\">");
        #self.write("window.parent.CKEDITOR.tools.callFunction(" + callback + ",'" + '/file?filename='+ filename + "',''" + ")");
        #self.write("</script>");