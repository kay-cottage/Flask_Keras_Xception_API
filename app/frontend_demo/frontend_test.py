  
import requests
import base64
import json
 
url = input('请输入API的URL:')
#url = 'http://192.18.31.31:5000/api/identify'

try:
    files = {"pic":open("2.jpg","rb")}
    response = requests.post(url,files = files)
    print('上传成功')
    print(json.loads(response.text))
except:
    print('上传失败，请重新检查操作')
