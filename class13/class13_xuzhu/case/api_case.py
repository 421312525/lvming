'''
@author:lvming
@time:2021/7/1
'''
#
import unittest
import requests
from class13.class13_xuzhu.api_keyword.api_key import ApiKey
from ddt import ddt,file_data
@ddt
class ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()
    # def setUp(self) -> None:  接口中基本不会用到setUp,会用到setUpClass
        # ak = ApiKey()
    @file_data('../data/user.yaml')
    def test_1(self,user,msg):
        # ak = ApiKey() 提取到前置
        url = 'http://39.98.138.157:5000/api/login'
        data = {
            'username':user['username'],
            'password':user['password']
        }
        res = self.ak.do_post(url=url,json=data)
        print(res.text)
        # 获取响应中的结果，用于校验是否成功
        # name = res.json()['info']['name']
        # print(name)
        # self.assertEqual(res.status_code,200,msg='请求错误') #不用这个断言了
        msg1 = self.ak.get_text(res.text,'msg')
        self.assertEqual(msg1,msg,msg='异常')

if __name__ == '__main__':
    unittest.main()