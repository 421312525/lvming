'''
@author:lvming
@time:2021/6/29
'''
# 测试登录  哪个知识点 unittest/pytest
import unittest

# 必须要继承unittest.TestCase
from class12.app09over.common.design import appium_yaml_conf
from class12.app09over.page.login_page import Login
from ddt import ddt,data,unpack,file_data


class Case(unittest.TestCase):
    # 用例执行前做的事 一个功能  流程  登录—选择商品—添加到购物车—下单
    # 启动程序
    def setUp(self) -> None:
        self.driver=appium_yaml_conf()

    def tearDown(self) -> None:
        self.driver.close()

    @file_data('../data/login.yaml')
    def test_login1(self,uname,upass):
        do = Login(self.driver)
        do.login(uname,upass)
        self.assertTrue(do.login_status(),msg='登录失败')

    @unittest.skip
    def test_login1(self):
        pass

# 执行用例 测试一条用例 App自动化 toast 配置参数

# 检测  登录成功没有  再去写个方法
if __name__ == '__main__':
    unittest.main()

# 总结：
# 1.启动程序，常用的方法取消 跳过  写在公共文件
# 2.取消 跳过会用到 点击 找元素内容 简洁 没有冗余 把基本的操作封装 BaseView
# 3.登录页面 支付页面 流程页面 pom页面对象 页面元素 页面流程 一个个的页面里面
# 4.测试用例 测什么东西 登录 unittest/pytest 一个流程 函数里面 登录，选择商品
# 5.很多测试数据 data文件夹

# 页面元素和流程分开
