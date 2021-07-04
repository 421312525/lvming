'''
@author:lvming
@time:2021/7/1
'''
import requests

'''
    课程回顾：
   1.接口关键字封装
   2.JsonPath库应用
接口关联：
   token与session是在接口端常用的鉴权机制
   很多的接口彼此之间是有关系的。通过token或者来进行确认。说白了。接口的关联其实就是特定数据的传递。
   基于session是通过requests.session()对象来实现数据的关联性
   基于token是通过变量的保存和传递来实现数据的关联性
'''
# 接口关联案例
# url = 'http://39.98.138.157:5000/api/login'
# data = {
#     'username':'admin',
#     'password':'123456'
# }
# res = requests.post(url=url,json=data)
# print(res.text)
#
# url = 'http://39.98.138.157:5000/api/getuserinfo'
# headers = {
#     'token':res.json()['token']
# }
# res = requests.get(url=url,headers=headers)
# print(res.text)


# 基于session来实现接口关联的方案：session的创建意味着，基于这个session所产生的相关session信息，都会被保存
session = requests.session()
print(session.cookies)
url = 'http://39.98.138.157:5000/api/login'
data = {
    'username':'admin',
    'password':'123456'
}
res = session.post(url=url,json=data)
print(res.text)
# session.get()
# session.post()
url1 = 'http://39.98.138.157:5000/api/getuserinfo'
res1 = session.get(url=url1)
print(session.cookies)
print(res1.text)







