'''
@author:lvming
@time:2021/7/2
'''
'''
    接口测试的操作执行核心：
	1.准备数据
	2.发送请求
	3.判断响应
'''
import unittest
from class13.class13_xuzhu.api_keyword.api_key import ApiKey
from ddt import ddt,file_data

from class13.class13_xuzhu.json_path.conf.read_ini import read_ini

@ddt
class CaseDemo(unittest.TestCase):
    # 关联数据赋值行为
    def assignment(self,kwargs):
        for key,value in kwargs.items():
            # 基于数据内容的格式来进行判断该用何种处理方式
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self,key)
        return kwargs
    # 定义接口中关联的全局变量
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()
        cls.url = read_ini('./json_path/conf/conf.ini','TEST_SERVER','url')
        cls.token = None
        cls.userid = None
        cls.openid = None
        cls.cartid = None

    # 测试用例的定义:Login接口的测试用例
    @file_data('./data1/user1.yaml')
    def test_1(self,path,data):
        url = self.url + path
        # data = {
        #     data['username'],
        #     data['password']
        # }
        res = self.ak.do_post(url=url,json=data)
        # print(res.text)
        # 赋值全局变量，把token变成全局变量，这样test_2可以拿到
        # 类名+变量名的方式进行赋值才可以修改全局变量的值
        token = self.ak.get_text(res.text, 'token')
        if token:
            CaseDemo.token = token
        # print(self.token)
        # print(res.text)

    # getuserinfo接口的测试用例
    @file_data('./data1/userinfo.yaml')
    def test_2(self,path,headers):
        url = self.url + path
        headers['token'] = self.token
        # print(headers)
        res = self.ak.do_get(url=url,headers=headers)
        # print(res.text)
        userid = self.ak.get_text(res.text, 'userid')
        openid = self.ak.get_text(res.text, 'openid')
        # print(userid,openid)
        if userid:
            CaseDemo.userid = str(userid)
        if openid:
            CaseDemo.openid = openid
        # print(res.text)

    # addcart接口测试用例
    @file_data('./data1/addcart.yaml')
    def test_3(self,path,headers,data):
        url = self.url + path
        # print(url)
        headers['token'] = self.token
        data['userid'] = self.userid
        data['openid'] = self.openid
        # print(self.openid,self.userid,data,path,url)
        res = self.ak.do_post(url=url,json=data,headers=headers)
        print(res.text)
        cartid = self.ak.get_text(res.text, 'cartid')
        productid = self.ak.get_text(res.text, 'productid')
        if cartid:
            CaseDemo.cartid = cartid
        if productid:
            CaseDemo.productid = productid


    # createorder接口测试用例
    @file_data('./data1/createorder.yaml')
    # def test_4(self,path,headers,data):
    def test_4(self,path,**kwargs):
        url = self.url + path
        # headers['token'] = self.token
        # data['userid'] = self.userid
        # data['openid'] = self.openid
        # data['cartid'] = self.cartid
        value = self.assignment(kwargs)
        # res = self.ak.do_post(url=url,headers=headers,json=data)
        res = self.ak.do_post(url=url,headers=value['headers'],json=value['data'])
        print(res.text)



if __name__ == '__main__':
    unittest.main()

# Excel与Yaml数据驱动：
#    Excel：
#       一次定型，后续操作技术需求量比较小
#       缺点在于不好维护
#    Yaml：
#        维护非常轻便
#        学习成本高
# 课后作业：
#    1.实现接口框架下关联接口的自动化测试
#    2.结合测试套件、HTMLTestRunner完善今天的测试框架
#    3.考虑单接口自动化测试框架的实现与覆盖
