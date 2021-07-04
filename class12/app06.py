'''
@author:lvming
@time:2021/6/29
'''
import time

from appium import webdriver
# appium继承了selenium

# 参数信息写好
from appium.webdriver.common.touch_action import TouchAction

info = {
    # 操作平台        安卓  苹果 Android不区分大小写，但不能写错
    'platformName':'Android',
    # 版本号
    'platformVersion':'7.1.2',
    # 设备名 adb devices 检测设备名  可以随意写，不要空，不要中文
    'deviceName':'127.0.0.1:62001',
    # 包名
    'appPackage':'com.android.settings',
    # 应用名
    'appActivity':'com.android.settings.ChooseLockPattern',
    # 不重置
    'noReset':False
}
# 启动程序 Remote(服务器,手机配置信息)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)

# 移动
TouchAction(driver).press(x=187,y=774).wait(1000).move_to(x=719,y=771)\
    .wait(1000).move_to(x=187,y=1306).wait(1000).move_to(x=719,y=1306).release().perform()

# 指针位置：开发者选项 指针位置
# #作业：实现考研帮的登录 账号 密码qwerty2664 qwerty123