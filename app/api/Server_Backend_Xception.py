# coding:utf-8
import os
import json
import time as t
from keras.applications.xception import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.backend import set_session



global sess
global graph


print('by kayak')
print('On GitHub:https://github.com/kay-cottage/Flask_Keras_Xception_API')
print('************************************************')
print('请正确配置classes.txt文件内的识别种类名称')
print('请正确配置好model_source文件夹下的模型文件')
print('请正确配置好templates文件夹下的html文件')
print('上传识别的图片被存于upload文件夹下')
print('************************************************')



#model_path = input(r'请正确输入模型文件的路径（model_path):')
model_path = r'model_source\model_fine_ep68_xception_cell_4.h5'
print('正在启动tensorflow加载模型文件，请稍等...')
sess = tf.Session()
graph = tf.get_default_graph()
set_session(sess)
model = load_model(model_path)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'


#读取识别种类
classes = []
with open(r"classes.txt", 'r') as f:
    classes = list(map(lambda x: x.strip(), f.readlines()))
    print(classes)
    list_long = 3 * int(len(classes)) + 1
    li = format(list_long, '1f')



@app.route("/uploader", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        start_time = t.time()
        f = request.files['file']
        if f is None:
            return "图片上传失败，无法识别(failed)"
        global file_path
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        end_time = t.time()
        used_time = end_time - start_time
        print(file_path + '图片用时%.3f s上传成功(file upload successfully)' % used_time)
        data = predi(file_path)
        return json.dumps(data)
    else:
        return {"code":405,
                "msg":"Method Not Allowed"
                }





@app.route('/upload')
def upload_file():
    return render_template('upload2.html')





def predi(file_path):
    print('loading picture(正在加载识别图片）')
    # load an input image
    start_time1 = t.time()
    img = image.load_img(file_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    with graph.as_default():
        set_session(sess)
        pred = model.predict(x)[0]
        result = [(classes[i], float(pred[i]) * 100.0) for i in range(len(pred))]
        end_time1 = t.time()
        used_time1 = end_time1 - start_time1
        print('识别图片过程用时%.2f s(predict successfully)' % used_time1)
        result.sort(reverse=True, key=lambda x: x[1])
        for i in range(0, 3):
            (class_name, prob) = result[i]
            print("Top %d ====================" % (i + 1))
            print("Class name: %s" % (class_name))
            print("Probability: %.3f%%" % (prob))
   
    data = {'code': 200,
            'msg': "success",
            'img_path': file_path,
            'result': result
            }
    print('************************************************')
    return data




# 启动路由
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
