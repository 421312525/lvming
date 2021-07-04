'''
@author:lvming
@time:2021/6/30
'''
'''
    接口概念：
  其实就是系统提供服务的一种形式，在现阶段企业中，所有软件都是基于前后端分离的形式来实现的。Client/Server
   1.接口是不需要有界面的存在即可直接运行
   2.前端下发的内容叫做请求(request)，经由特定渠道进行传输，发送至后端服务器，服务器进行运算和处理，产生响应结果(response)并原路返回至前端
   3.所有的接口都是基于请求来激活，而且一定会产生响应
  由接口产生出的概念：
      1.如何定位到准确的接口:url，接口的路径，也就是path
	URN：统一资源名称
	url：统一资源定位符
	uri：统一资源标识符
      2.网络协议：规矩的存在
	80~90的系统结构下，都是基于HTTP网络协议来进行实现的。
	目前普遍应用的HTTP1.1的版本，tcp协议之上的一种网络协议，如果承载有SSL协议的基础上，就形成HTTPS网络协议
	http协议下的url的格式定义：
	   网络协议：//IP:PATH?args=xxx&args2=xxx
	http://39.98.138.157:5000/api/getuserinfo
	http与https网络协议下有默认端口，分别是80，443
	请求方法(method)：
	   get：查询、获取数据列表、铭文传递所有数据(数据在url中直观显示)
	   post：提交、更新、修改、插入对数据进行变动和提交的动作，暗中交易各种数据(数据在体内流转)
	所有的http协议下的请求，都是无状态的。
	所以我们需要有接住cookie、session、token的鉴权机制来确保状态是持续的。
	在协议下，所有的请求简单理解为是一次性产物
	token：一般保存在请求头或者身体中。身份令牌的形式
	session：保存在服务端的一个临时回话，所有通信都是基于已创建的session来进行通信，具有时效性，时间过期或者主动销毁，则session消失
	cookies：本地文件保存
	请求内容：
	   1.头(headers)：定义本次传输的所有规范
	   2.身体(body)：用于传输的数据，一般是post   
	HTTP版本在2.x的模式下，有长连接的状态
	TCP协议下的接口通信，一般用于C/S架构下的接口数据通信
   Dubbo、RPC、restful、微服务
   Dubbo、微服务架构、RPC
   微服务架构
	服务器提供服务，分布式(负载均衡)，路由网关，子节点
	RPC(remote proceduce call)远程过程调用
	主体是前端与路由网关进行交互的过程，也是基于HTTp协议，内部的通信协议可能是tcp也可能是http
   	restful：本身只是一种规范化的格式
	   基于HTTP网络协议下的接口通信
'''