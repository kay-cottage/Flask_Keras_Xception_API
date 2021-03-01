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
global data

sess = tf.Session()
graph = tf.get_default_graph()
set_session(sess)
model_path = r'model_source\model_fine_ep68_xception_cell_4.h5'
model = load_model(model_path)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['DB_FOLDER'] = 'dbupload/'


#读取识别种类
classes = []
with open(r"classes.txt", 'r') as f:
    classes = list(map(lambda x: x.strip(), f.readlines()))
    print(classes)
    list_long = 3 * int(len(classes)) + 1
    li = format(list_long, '1f')


#识别接口
@app.route("/api/identify", methods=["GET", "POST"])
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
        predi()
        return json.dumps(data)
    else:
        errordata = {"code":405,
                "msg":"Method Not Allowed"
                }
        return json.dumps(errordata)

    

#数据集上传接口(上传数据集压缩文件）   
@app.route("/api/dbupload", methods=["GET", "POST"])
def dbupload():
    if request.method == 'POST':
        start_time = t.time()
        f1 = request.files['file']
        if f1 is None:
            return "文件上传失败"
        global data_file_path
        data_file_path = os.path.join(app.config['DB_FOLDER'], secure_filename(f1.filename))
        f.save(os.path.join(app.config['DB_FOLDER'], secure_filename(f1.filename)))
        end_time = t.time()
        used_time = end_time - start_time
        print(file_path + '文件用时%.3f s上传成功(file upload successfully)' % used_time)
        dbdata = {"code":200,
                "msg":"success"
                }
        return json.dumps(dbdata)
    else:
        errordata = {"code":405,
                "msg":"Method Not Allowed"
                }
        return json.dumps(errordata)



@app.route('/upload')
def upload_file():
    return render_template('upload.html')




#预测函数
def predi():
    global model
    # load an input image
    print('loading picture(正在加载识别图片）')
    # load an input image
    start_time1 = t.time()
    img = image.load_img(file_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    #print(x)
    with graph.as_default():
        set_session(sess)
        pred = model.predict(x)[0]
        #print('prediction:',pred)
        global result
        result = [(classes[i], float(pred[i]) * 100.0) for i in range(len(pred))]
        end_time1 = t.time()
        used_time1 = end_time1 - start_time1
        print('识别图片过程用时%.2f s(predict successfully)' % used_time1)
        print('result:',result)
        global data
        data = {'code':200,
                'msg':"success",
                'img_path': file_path,
                'result':result
                }
        result.sort(reverse=True, key=lambda x: x[1])
        for i in range(0, 3):
            (class_name, prob) = result[i]
            print("Top %d ====================" % (i + 1))
            print("Class name: %s" % (class_name))
            print("Probability: %.3f%%" % (prob))
    print('json:',json.dumps(data))
    print(t.strftime('%Y-%m-%d-%H:%M:%S',t.localtime()))
    print('##############################################')
    return json.dumps(data)




# 启动路由
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

