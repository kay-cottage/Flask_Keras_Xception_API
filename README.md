# Flask_Keras_Xception_API
使用Flask部署的基于Keras的Xception神经网络实现细胞种类图像AI医疗辅助识别系统（含简单前端demo）


微信小程序版识别演示视频请见：https://www.bilibili.com/video/BV1pf4y147er


网页版识别程序演示视频请见：https://www.bilibili.com/video/BV12A411T7bu


# 简介 #

An API with Xception which can identify a variety of cells images.


基于Flask搭建的Xception深度可分离卷积神经网络训练的细胞形态识别的API接口（更换网络模型也可以识别多种不同类型的图像）。通过部署在云服务器，在并发量较小的情况下，能过作为第三方接口被APP，微信小程序（WechatMiniProgramme）等调用，较快速地对客户端上传的图片进行准确的识别并返回结果！


含有带有标签的图像数据集的上传接口供使用者上传以用作神经网络的训练，提升神经网络的识别种类与中准确度！


目前能够比较准确识别（测试集准确率大于90%）嗜酸性粒细胞，嗜碱性粒细胞，中性粒细胞，与成熟红细胞4种！或者嗜酸性粒细胞，嗜碱性粒细胞，中性粒细胞，成熟红细胞，淋巴细胞，单核细胞与浆细胞7种！（后三者为差别更小的细粒度图像识别，由于数据非常有限，准确率有待提高!)



目前由于训练集数据非常有限，识别种类有待增多，欢迎大家前来改进模型，提供更多数据！


为个人想法的简单实现，旨在让更多人方便地用上AI细胞识别技术辅助诊断！


*注意：禁止用于商业用途，欢迎个人学习交流！*







# 使用方法 #



*该项目是能够对http请求做出响应的深度学习图像识别的（API）应用程序接口*



1.请先在python安装好相应需要导入的库【或者直接下载安装包（下载链接请见下方链接）进行安装】，然后通过以下链接下载已训练好的Xception神经网络模型，（4种细胞识别）并放入到目录model_source下。


模型文件链接：https://pan.baidu.com/s/1hdLoYS51IqcdVhB01w2yDw 提取码：X1z9




2.检查文件夹classes.txt文件中是否有需要识别细胞的类别名称（英文），即RBC，eosinophi，basophil，neutrophil！（claesses.txt是用来存放被识别物体种类名称的文件）


3.启动程序Server_Backend_Xception.py(或者启动Server_Backend_Xception.exe），通过浏览器端访问API路径（例如： http://example.com:5000/upload ） 得到请求页面，选择需要识别的图片上传，等待返回识别结果即可！又或者通过APP，微信小程序调用【例如http://example.com:5000/api/identify （识别接口） 或者 http://example.com:5000/api/dbupload （数据集上传接口）】 接口使用即可


# 相关下载资源 #
X64版本软件安装包（Setup.exe）

下载链接：https://github.com/kay-cottage/Flask_Keras_Xception_API/releases/download/V1.0/Flask_Xception_API_V1.0_X64.exe


X64版本软件压缩包(.zip)

下载链接：https://github.com/kay-cottage/Flask_Keras_Xception_API/releases/download/v1.0/Flask_Xception_API.zip

4种细胞识别神经网络模型（准确率更高）

下载链接：https://pan.baidu.com/s/1hdLoYS51IqcdVhB01w2yDw 提取码：X1z9


7种细胞识别神经网络模型

下载链接链接：https://pan.baidu.com/s/1xY5C5x9iDkS-dr2QGtcGng 提取码：X1z9


# 补充（注意事项）#


1.项目中Server_Backend_Xception.py/Server_Backend_Xception.exe文件为API服务器端程序，返回json类型格式识别结果。


2.请在templates文件夹下内放置html文件，Server_Backend_Xception.py调用该目录下的upload页面


3.使用POST请求才能正确返回识别结果，如果使用GET等请求会返回错误代码，请正确设置请求方式！


4.注意：该程序初次加载模型启动时候需要一段时间（10s或更长），请耐心等待！


视频版本效果演示欢迎访问我的bilibili主页查看：https://space.bilibili.com/362186371 更多相关项目视频敬请期待！


最后，不喜勿喷，谢谢！
