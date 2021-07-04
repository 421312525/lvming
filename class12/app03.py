'''
@author:lvming
@time:2021/6/28
'''
# python代码实现启动程序定位
# 安装pip.exe install appium-python-client  或者setting里面安装
'''
    注意：模拟器：设置竖屏
    会造成appium截图是个倒面板
    
    http://appium.io/docs/en/writing-running-appium/caps/
    
    查包名： 1.aapt  2.adb shell pm list packages
    3.adb shell dumpsys window w |grep name=
    
    
    uiautomatorviewer找不到模拟器设备 模拟器也连接好了
'''
import time

from appium import webdriver
# appium继承了selenium

# 参数信息写好
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
    'appActivity':'com.android.settings.Settings',
    # 不重置
    'noReset':False
}
# 启动程序 Remote(服务器,手机配置信息)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)

# 元素定位 常用id class xpath
# 点击搜索
# driver.find_element_by_id('com.android.settings:id/search').click()
# class_name
# driver.find_element_by_class_name('com.android.settings:id/search').click()
# 点击搜索 xpath
# driver.find_elements_by_xpath('//*[@content-desc="搜索"]').click()
# accessibility_id
# driver.find_element_by_accessibility_id('搜索').click()
# android_uiautomator id class text
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.settings:id/search")').click()
# time.sleep(3)
# # 组合在一起 实现搜索 秋水 返回
# driver.find_element_by_id('com.android.settings:id/search').click()
# driver.find_element_by_class_name('android.widget.EditText').send_keys('秋水')
# # 返回
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()

# 一次性定位到很多值
titles = driver.find_elements_by_class_name('android.widget.TextView')
# 打印有多少个
print(len(titles))
# 把内容都打印出来
for title in titles:
    print(title.text)
# 下标
titles[4].click()

# 等待几秒钟 等待3种方式 隐式等待 显示等待 强制等待
time.sleep(3)

# 关闭
driver.quit()