'''
@author:lvming
@time:2021/6/29
'''
# App常用操作 滑动 拖拽操作时间
# 应用场景：做app有些界面或者按钮需要滑动才会出来
# 滑动：
# swipe
# scroll
# drag_and_drop
#
#
# swipe 写法 swipe(开始x左标，开始y左标，结束x左标，结束y左标)

import time

from appium import webdriver
# appium继承了selenium

# 参数信息写好
info = {
    # 操作平台        安卓  苹果 Android不区分大小写，但不能写错
    'platformName':'Android',
    # 版本号
    'platformVersion':'10',
    # 设备名 adb devices 检测设备名  可以随意写，不要空，不要中文
    'deviceName':'1999e3ac',
    # 包名
    'appPackage':'com.android.settings',
    # 应用名
    'appActivity':'com.android.settings.Settings',
    # 不重置
    'noReset':False
}
# 启动程序 Remote(服务器,手机配置信息)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.implicitly_wait(5)

# swipe 写法 swipe(开始x左标，开始y左标，结束x左标，结束y左标)
# 产生惯性 持续时间越长，惯性越小
# driver.swipe(479,2179,517,736)
# driver.swipe(479,2179,517,736,3000)

# 元素滑动
# scroll(开始元素，结束元素)
# scroll滑动：从一个元素滑动到另外一个元素 也有惯性
voice = driver.find_element_by_xpath('//*[@text="动态效果"]')
fly = driver.find_element_by_xpath('//*[@text="150****4959"]')
# driver.scroll(voice,fly)

# drag_and_drop：从一个元素滑动到另外一个元素 没有惯性
# 可以滑动 实现滑动 选择 需不需要惯性，选择用左标还是用元素
driver.drag_and_drop(voice,fly)

time.sleep(5)
driver.quit()