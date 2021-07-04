'''
@author:lvming
@time:2021/6/30
'''
# 接口（二） requests库
'''
        接口的分类
       硬件接口：USB、VGA、HDMI等等
       软件接口：
          本地接口：windows系统API，Android SDK等等
          网络接口：
             传输层：基于TCP的私有协议接口
             应用层：webservice、RESTful
    目前在企业的测试中，基本上所说的接口都是网络接口。
    
    URI和URL
    URI-统一资源标识符
    URI是某个协议方案表示的资源的定位标识符。协议方案是指访问资源所使用的协议类型名称。
    URL是URI的一个子集
    URI格式：
    http://user:pass@www.example.jp:80/dir/index.html?uid=1#ch1
    协议方案名、登录信息(认证)、服务器地址、服务器端口号、带层次的文件路径、查询字符串、片段标识符
    
    http协议用于客户端和服务端之间的通信
    通过请求和响应的交换达成通信
    
    请求报文的格式
    方法：  uri   协议版本
    
    请求方法
    GET：获取资源
    POST：传输实体数据
    PUT：传输文件
    HEAD：获取报文首部
    DELETE：删除文件
    OPTIONS：询问支持的方式
    TRACE：追踪路径-不常用
    CONNECT：加密让数据更安全
'''
'''
    2xx 成功
    200 成功
    204  No Content请求处理成功！但没有资源可返回
    206 Partial Content 是对资源某一部分的请求
    
    3xx 重定向
    301 Moved Permanently
    需要进行书签引用的变更，已更新成功
    302 Found 
    资源的url已临时定位到其它位置
    304 Not Modified
    附带条件的请求。资源已找到，但未符合条件请求
    
    4xx客户端错误
    400 Bad Request
    401 Unauthorized 客户端没有权限
    403 Forbidden 这个资源是禁止访问的
    404 Not Found 没有找到资源
    
    5xx服务端错误
    500 Internal Server Error 服务端临时故障
    
    HTTP特点
    HTTP是一个无状态协议
    解决HTTP的无状态问题
    
    Token是服务器端生成的令牌，用算法和密钥做了一个签名
'''
import requests
import json

# requests.get('https://api.github.com/events')
# requests.post('http://httpbin.org/post',data={'key': 'value'})

# 传递url参数  -  GET请求
# payload = {'key1': 'value1','key2':'value2'}
# payload = {'key1': 'value1','key2':['value2','value3']}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.url)

# 响应的内容
# r = requests.get('https://api.github.com/events')
# print(type(r.text))
#
# # JSON响应内容
# r = requests.get('https://api.github.com/events')
# json_data = r.json()
# print(json_data)
# print(type(json_data))
#
# # 通过json模块来进行转换
# r = requests.get('https://api.github.com/events')
# 将JSON字符串转换成python数据类型json.loads()
# json_data = json.loads(r.text)
# print(json_data)
# print(type(json_data))

# 稍微复杂的post请求
# 在调用post方法时，给data关键字参数赋值python字典对象，相当于提交表单数据
#
# payload = {'key1': 'value1','key2':'value2'}
# r = requests.post("http://httpbin.org/post",data=payload)
# print(r.text)
# print(r.status_code)

# post请求赋值2种方式1：
# payload = {'password': '123456','name':'admin'}
# # r = requests.post("http://127.0.0.1:8008/login",data=payload)
# 在调用post方法时，给json关键字参数赋值python字典对象
# r = requests.post("http://127.0.0.1:8008/login",json=payload)
# print(r.text)

# post请求赋值2种方式2：
# 在调用post方法时，给data关键字参数赋值json字符串
# payload = {'password': '123456','name':'admin'}
# # 将字典转换成json字符串
# payload_json = json.dumps(payload)
# print(type(payload_json))
# r = requests.post("http://127.0.0.1:8008/login",data=payload_json)
# # r = requests.post("http://127.0.0.1:8008/login",json=payload)
# print(r.text)
# print(r.status_code)


# 设置请求的请求头
payload = {'key1': 'value1','key2':'value2'}
headers = {"Content-Type": "application/json"}
r = requests.post("http://httpbin.org/post",json=payload,headers=headers)
print(r.text)
print(r.status_code)