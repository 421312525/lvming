'''
@author:lvming
@time:2021/7/1
'''
import unittest
from unittest import mock
import requests
from class13.class13_xuzhu import demo03
from class13.class13_xuzhu.demo03 import plus


class Demo(unittest.TestCase):
    # 常规形态下的mock实现
    def test_01(self):
        demo03.plus = mock.Mock(return_value=2)
        c = demo03.plus(1,2)
        # d = demo03.math()
        print(c)
    # 基于装饰器的形态来实现的mock,对应哪个接口需要mock
    @mock.patch('demo03.login')
    def test_02(self,mock_login):
        # 已经完成了Mock数据的生成:mock的操作相当于自主定义生成测试数据，快速提供至测试行为之中
        a= mock_login.return_value = {'username':'admin','password':'123456'}
        # txt = demo03.login()
        print(a)
        res = requests.post(url='http://39.98.138.157:5000/api/login',json=a)
        print(res.text)

    # mock实现形式3：如果要实现多次调用，每次有不同的值
    @mock.patch.object(demo03,'plus')
    def test_3(self,mock_plus):
        mock_plus.side_effect={
            'plus1',
            'plus2',
            'plus3',
        }
        for i in range(0,2):
            demo03.math()

if __name__ == '__main__':
    unittest.main()