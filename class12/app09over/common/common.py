'''
@author:lvming
@time:2021/6/29
'''
# 运用到pom思想 页面元素分离出来
# 页面元素经常变化 页面元素可提取出来
from time import sleep
from selenium.webdriver.common.by import By
from class12.app09over.common.design import appium_yaml_conf
from class12.app09over.BaseView.base_view import BaseView

class Common(BaseView):

    # 同意的元素
    agree1=(By.XPATH,'//*[@text="同意并开启以上权限"]')
    into=(By.XPATH,'//*[@text="进入地图"]')
    allow1 = (By.XPATH, '//*[@text="允许"]')
    allow2=(By.XPATH,'//*[@text="始终允许"]')
    allow3=(By.XPATH,'//*[@text="允许"]')

    def agree(self):
        try:
            self.on_click(self.agree1)
            self.on_click(self.into)
            self.on_click(self.allow1)
            self.on_click(self.allow2)
            self.on_click(self.allow3)
        except Exception as e:
            print('没有同意页面')
    # 获得窗口大小
    def get_size(self):
        x=self.window_size()['x']
        y=self.window_size()['y']
        return x,y
    # 滑动
    def swipe_left(self):
        le=self.get_size()
        x1 = le[0]*0.9
        y1 = le[1]*0.5
        x2 = le[2]*0.2
        self.swipe(x1,y1,x2,y1,1000)

if __name__ == '__main__':
    # 先启动程序
    driver = appium_yaml_conf()
    # 点击跳过
    com = Common(driver)
    com.agree()

# 登录的操作
# 登录页面 支付页面 下单页面 购物页面
# pom
