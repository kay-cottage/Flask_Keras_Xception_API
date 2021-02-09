#GUI by Charon
import requests
import base64
import json
import easygui as g
import sys

url = g.enterbox(msg='请输入API的URL:')
#url = 'http://192.18.31.31:5000/'

while 1:
    if g.ccbox('请选择',choices = ('选择图片路径','退出')):
        file_path = g.fileopenbox();
        #g.msgxob(file_name)
        try:
            files = {"pic":open(file_path,"rb")}
            response = requests.post(url,files = files)
            g.msgbox('上传成功，识别结果为')
            g.msgbox(str(json.loads(response.text)))
        except:
            g.msgbox('上传失败，请重新检查操作')
    else:
        sys.exit(0)
