'''
@author:lvming
@time:2021/6/29
'''
# 高级手势 TouchAction
# 基本的手势组合在一起变成高级手势 基本的手势 移动，按下，抬起，轻敲
# 步骤
from appium.webdriver.common.touch_action import TouchAction

'''
1.创建一个touchAction对象
2.对象调用我们想要做的操作
3.通过perform()
'''

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

# 基本事件  轻敲(元素)
# 模拟对蓝牙进行轻敲
# bluntooth=driver.find_element_by_xpath('//*[@text="WLAN"]')
# action=TouchAction(driver)
# action.tap(bluntooth)
# action.perform()

# action=TouchAction(driver)
# action.tap(x=293,y=992)
# action.perform()

# TouchAction(driver).tap(x=293,y=992).perform()

# 按下和抬起 press()按下  抬起release()
# time.sleep(1)
# TouchAction(driver).press(x=996,y=987).release().perform()
# time.sleep(5)

# 等待
# TouchAction(driver).press(x=996,y=987).wait(1000).release().perform()
