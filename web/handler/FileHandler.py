# coding:utf8

from BaseHandler import BaseHandler

import os

'''
文件上传下载处理类
'''

class FileHandler(BaseHandler):

    def get(self):
        '''
        文件下载
        '''
        filename = self.get_argument('filename', default='')
        if filename == '':
            self.write('')
            return
        filename = os.path.join(os.path.abspath('view/static/upload'),filename)

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
        upload_path=os.path.join(os.path.abspath('view/static/upload')) 
        #提取表单中‘name’为‘upload’的文件元数据
        file_metas=self.request.files['upload']
        callback = self.get_argument("CKEditorFuncNum"); 
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            #有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath,'wb') as up:      
                up.write(meta['body'])
            #self.write('/file?filename='+ filename) #直接输出上传文件的URL地址
            #下面调用CKEDITOR的函数，为URL赋值
            self.write("<script type=\"text/javascript\">");
            self.write("window.parent.CKEDITOR.tools.callFunction(" + callback + ",'" + '/file?filename='+ filename + "',''" + ")");
            self.write("</script>");