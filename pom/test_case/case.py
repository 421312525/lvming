'''
@author:lvming
@time:2021/6/28
'''
from time import sleep

from ddt import ddt,file_data
from selenium import webdriver
from pom.page_object.cart_page import CartPage
from pom.page_object.login_page import LoginPage
from pom.page_object.phone_product_page import PhonePage

'''
    测试用例类，所有的测试代码都在该类实现
'''
import unittest
@ddt
class Case(unittest.TestCase):
    #前置条件
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)
    # 用例
    # def test_shopxo(self):
    #     driver = webdriver.Chrome()
    #     lp = LoginPage(driver)
    #     pp = PhonePage(driver)
    #     cp = CartPage(driver)
    #     user = 'xuzhu666'
    #     pwd = '123456'
    #     lp.login(user,pwd)
    #     pp.add_cart()
    #     cp.cart_info()
    #     # status = cp.cart_info()
    #     print('执行成功')
    #     sleep(5)
    #     # self.assertTrue(status)
    # 登录
    @file_data('../data/login.yaml')
    def test_01_login(self,user,pwd):
        self.lp.login(user,pwd)

    # 添加商品
    def test_02_add_cart(self):
        self.pp.add_cart()

    # 购物车校验
    def test_03_assert_cart(self):
        self.cp.cart_info()
        self.pp.check('1')
        # self.pp.check('2')



if __name__ == '__main__':
    unittest.main()