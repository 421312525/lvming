'''
@author:lvming
@time:2021/7/1
'''

'''
    课程回顾：
	1.讲解了有关接口测试的相关概念与Requests库的应用
		1.参数的类型处理，有需要转换为json的记得转换。
		2.忽略了头部信息的修改添加(content-type)
接口鉴权机制：
token-session-cookie的鉴权机制
接口本身具备有的鉴权，是基于Authorization来进行鉴权的。
接口请求：
   1.与服务端建立通信
   2.基于协议传递数据
   3.解析生成结果并返回

MD5加密：
   在HTTP请求下，所有的数据都是通过协议渠道进行传递，虽然post请求下，所有数据都是在body进行传递
   HTTP+S网络协议
   主流的加密形态是MD5加密形式 一种单向通道的加密算法
   在python中实现MD5加密形式数据处理方法：通过hashlib
'''
# 导入MD5加密的库
import hashlib

# arg = '小明爱颖颖'
# print(arg)
# # md5加密的实现形式
# secret = hashlib.md5(arg.encode('utf-8'))
# # 获取变量的内存地址
# print(secret)
# # 获取值
# print(secret.hexdigest())

# md5加密函数
def hashmd5(string):
    return hashlib.md5(str(string).encode('utf-8')).hexdigest()


