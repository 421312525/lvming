'''
@author:lvming
@time:2021/6/29
'''
# 考研帮登录实现

# 配置信息
import time

from appium import webdriver

info = {
    'platformName':'Android',
    'platformVersion':'7.1.2',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.tal.kaoyan',
    # 'appPackage':'name=com.vphone.launcher',
    'appActivity':'com.tal.kaoyan.ui.activity.ucenter.LoginActivity',
    'noReset':False
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)
def check_cancel():
    print('点击取消')
    try:
        driver.find_element_by_id('android:id/buttons').click()
        # logger.info()
    except Exception as e:
        # logger.error()
        print('没有取消按钮')
def check_skip():
    print('点击跳过')
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
        # logger.info()
    except Exception as e:
        # logger.error()
        print('没有跳过按钮')
def login():
    # 找到输入框输入用户名
    driver.find_element_by_xpath('//*[@text="请输入用户名"]').send_keys('qwerty2664')
    # 找到密码框输入密码
    driver.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('qwerty123')
    # 找到登录按钮进行点击
    driver.find_element_by_xpath('//*[@text="登录"]').click()

# 智能获取
# 1.屏幕大小
def size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(x,y)
    return x,y
# swipe(开始x坐标，开始y坐标，结束x坐标，结束y坐标)
# driver.swipe(834,954,224,1050)
# 右边x轴大，y轴小，坐标x小，y轴一样
def swipeLeft(n,t):
    size2 = size()
    print(size2,type(size2))
    x1 = size2[0] * 0.8
    y1 = size2[1] * 0.9
    x2 = size2[0] * 0.2
    for i in range(n):
        driver.swipe(x1,y1,x2,y1,t)

# check_cancel()
# check_skip()
login()
time.sleep(5)
driver.quit()

# 实现自动化的效果
# 项目结构 POM