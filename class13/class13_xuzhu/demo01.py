'''
@author:lvming
@time:2021/6/30
'''
from class13.class13_xuzhu.demo02 import hashmd5

'''
    接口测试思路：
   1.所有的接口都是基于S端来实现和提供服务的。所以所有的接口在执行测试的时候，都是只需要有后端的支持即可。
   2.通过直接模拟请求，下发知服务端，再接收服务端的响应，从而实现一次接口的调用，也意味着对接口的一次测试。
   3.软件的研发：
	需求分析-需求说明说-设计-前后端编码-两端联调-测试-发布-维护
	接口的测试不同于常规的测试手段和行为，所以不需要考虑前端的实现，在后端编码完成时即可介入测试
	抓包是在知道接口本身的情况下进行抓包
	通过请求的数据判断前端是否有问题，通过响应的结果判断后端是否有问题。
Requests库：
   Requests库本身就是基于urllib的基础上再进行的开源的HTTP协议的库，可以更加简单直接地进行HTTP请求的生成，和结果的处理
'''
'''
    requests库实现的接口测试应用：
	1.导包
	2.接口请求的模拟
	   1.确定协议是http/https
	   2.确定请求需传递的参数：通过api文档进行确认
	3.如果需要对请求的内容做一定限制，可以在参数中进行设置
	    json 表示传入json格式的参数
        timeout 表示本次接口的调用超时时长的定义
        headers 表示本次接口传输时的headers当时自定义添加的内容
    4.在requests库中，进行请求模拟时，请标注清晰每一个参数分别是什么
	   
    请求中会生成有http状态码：
    1xx  请求与你进行对接
    2xx  正常交互返回
    3xx  重定向
    4xx  路径异常
    5xx  服务器错误

'''
import requests
import json

# 接口请求的模拟
# 数据的生成
data = {
    'username':'admin',
    'password':hashmd5('123456')
}
data1 = {"city":"1"}
# 文件上传时的文件参数形式
file = {
    'file':open('../../class08/file/1.html','r',encoding='utf-8')
}
# Json是一种数据类型？
# json不是一种数据类型，只是一种特定格式内容的数据对象
# 将data转换为json对象：通过使用json库来进行转换
# dumps是进行转型，将原有的字典数据转换为json格式
jsonData = json.dumps(data)
print(jsonData)
# {
# 	"key1":"value1"
# }
# 请求头定义
headers = {'Content-Type': 'application/json'}
# 接口的地址
url = 'http://39.98.138.157:5000/api/login'
# 将数据传递到对应的接口地址，来实现一次该接口的请求下发并返回响应结果:定义对应的请求方法
res = requests.post(url=url,json=data,headers=headers)
# res1 = requests.get(url='http://39.98.138.157:5000/api/getweather',params=data1,timeout=1)
# res1 = requests.get(url='http://39.98.138.157:5000/api/getuserinfo',params=file,timeout=1)
# 输出是一个响应对象，默认显示响应吗
print(res)
# 输出状态码
print(res.status_code)
# 用于判断接口请求的状态码是否是200，如果是，则返回None，如果不是则返回异常,所有要调用时一定结合try….except运行
try:
    print(res.raise_for_status())
except Exception as e:
    print('返回码异常')
# assert 200 == res.status_code
# 输出响应结果：返回原始结果
# print(res.content)
# 输出响应结果:编译后的内容
# print(res.text)
# print(res1.json())
# 最原始的响应原始内容
# print(res.raw)
#
print(res.request.headers)
# print(res.request.body)

# 对响应结果进行内容的获取，并判断关键内容是否符合预期结果
# assert 'success' == res.text['msg']
# 数据进行转码
content = json.loads(res.text)
# assert 'success' == content['msg']
# print(type(content),content)
