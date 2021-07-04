'''
@author:lvming
@time:2021/6/29
'''
from selenium.webdriver.common.by import By

from class12.app09over.BaseView.base_view import BaseView
from class12.app09over.common.common import Common
from class12.app09over.common.design import appium_yaml_conf


class Login(Common):
    # 登录元素
    # 用户名
    username_type = (By.ID,'')
    # 密码
    password_type = (By.ID,'')
    # 登录按钮
    loginBtn_type = (By.ID,'')
    # 我自己的登录状态
    myself = (By.ID,'')

    # 登录的流程 输入用户名 输入密码 点击登录 常用方法登录
    def login(self,username,password):
        self.agree()
        self.on_input(self.username_type,username)
        self.on_input(self.password_type,password)
        self.on_click(self.loginBtn_type)

    #
    def check_alter(self):
        print('检查弹窗')

    # 检测登录状态的方法 可能会弹出一个弹窗 弹窗也要定位到
    def login_status(self):
        try:
            self.on_click(self.myself)
            self.locator(self.username_type)
        except Exception as e:
            print('登录失败')
            return False
        else:
            print('登录成功')
            # 退出的方法
            self.loginout()
            True
    # 退出登录
    def loginout(self):
        pass

if __name__ == '__main__':
    # 先启动程序
    driver = appium_yaml_conf()
    lo = Login(driver)
    lo.login()

# 登录的方法写完后，测试