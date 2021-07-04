'''
@author:lvming
@time:2021/6/29
'''
# 项目中基本的操作 封装在这个文件
# 输入 点击 找元素

from appium import webdriver
from class12.app09over.log.mylog import test_log
log = test_log()
class BaseView:
    def __init__(self,driver):
        # self.driver = webdriver.Remote()
        self.driver = driver
    # 元素定位 元组解析加*
    def locator(self,loc):
        return self.driver.find_element(*loc)
    # 输入 找到元素 在进行输入
    def on_input(self,loc,txt):
        try:
            log.info('定位{}元素，输入{}'.format(loc,txt))
            self.locator(loc).send_keys(txt)
        except Exception as e:
            log.error('输入失败')

    # 点击 找到元素 再进行点击
    def on_click(self,loc):
        self.locator(loc).click()
    # 等待
    def wait(self):
        self.driver.implicitly_wait(10)
    # 关闭
    def close(self):
        self.driver.quit()
    # 获取窗口大小
    def window_size(self):
        return self.driver.get_window_size()
    # 滑动
    def swipe(self,start_x,start_y,end_x,end_y):
        self.driver.swipe(start_x,start_y,end_x,end_y)

