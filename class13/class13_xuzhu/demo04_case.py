'''
@author:lvming
@time:2021/7/2
'''
import unittest

import requests


class ApiDemo(unittest.TestCase):
    # 实现接口关联的测试用例
    def test_1(self):
        # 通过登录接口获取token
        url = 'http://39.98.138.157:5000/api/login'
        data = {
            'username':'admin',
            'password':'123456'
        }
        res = requests.post(url=url,json=data)
        print(res.text)
        # 基于获取的token来实现信息的查找
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        headers = {
            'token': res.json()['token']
        }
        res1 = requests.get(url=url,headers=headers)
        print(res1.text)
        # 添加商品到购物车，基于token、userid、openid
        url = 'http://39.98.138.157:5000/api/addcart'
        headers = {
            'token':res.json()['token']
        }
        data = {
            'userid': res1.json()['data'][0]['userid'],
            'openid': res1.json()['data'][0]['openid'],
            'productid': 8888
        }
        res2 = requests.post(url=url,headers=headers,json=data)
        print(res2.text)
        # 购物车下单
        url = 'http://39.98.138.157:5000/api/createorder'
        headers = {
            'token':res.json()['token']
        }
        data = {
            'userid': res1.json()['data'][0]['userid'],
            'openid': res1.json()['data'][0]['openid'],
            'productid': 8888,
            'cartid': res2.json()['data'][0]['cartid']
        }
        res3 = requests.post(url=url,json=data,headers=headers)
        print(res3.text)
        self.assertEqual('success',res3.json()['result'],msg='流程异常')


if __name__ == '__main__':
    unittest.main()