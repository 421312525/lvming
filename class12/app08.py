'''
@author:lvming
@time:2021/6/29
'''
# 多点触控 multiAction，是touchAction的一个补充模块。更高级
# touchAction高级手势，一个手指移动
# 两个手指一起移动，多个点移动
# 百度底图 放大缩小
# TouchAction步骤
# 1.创建TouchAction对象
# 2.通过对象调用我们想要执行的操作
# 3.通过perform()执行

# MultiAction
# 步骤：
# 1.创建两个手指 创建2个TouchAction对象
# 2.创建MultiAction()对象
# 3.把2个TouchAction对象，添加进MulitAction()对象
# 4.通过perform()执行
from time import sleep

from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

info = {
    'platformName':'Android',
    'platforVersion':'10',
    'deviceName':'1999e3ac',
    'appPackage':'com.autonavi.minimap',
    'appActivity':'com.autonavi.map.activity.NewMapActivity',
    'noReset':False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
# 等待页面加载出来
driver.implicitly_wait(5)

def agree():
    driver.find_element_by_xpath('//*[@text="同意并开启以上权限"]').click()
def into():
    driver.find_element_by_xpath('//*[@text="进入地图"]').click()
def allow():
    driver.find_element_by_xpath('//*[@text="允许"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@text="始终允许"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@text="允许"]').click()




# 1.获得屏幕尺寸
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

# 2.缩小地图 放大地图

# 第一个手指头
action1 = TouchAction(driver)
l= action1.press(x=x*0.1,y=y*0.2).wait(1000).move_to(x=x*0.3,y=x*0.5).wait(1000).release()
# 第二个手指头
action2 = TouchAction(driver)
p= action2.press(x=x*0.5,y=y*0.7).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()

agree()
into()
allow()

# 执行缩小操作
sleep(5)
action1.tap(x=573,y=666)
sleep(1)
zoom = MultiAction(driver)
zoom.add(l,p)
zoom.perform()

if __name__ == '__main__':
    for i in range(3):
        pass

# 布置两个作业：
# 1.滑动 向左滑动 向右滑动 向上滑动 向下滑动
# 放大缩小  缩小  放大

# 混合apph5的定位
# app分为3类 原生的(JAVA) 混合的(JAVA+h5)  H5(HTML+CSS+JAVASCRIPT)
# 怎么去分辨  边界
# 不好去定位 content切换到webview模式
# 如果想做h5的元素操作
# 环境准备一下
# 1.下载uc-dectools工具
# 2.浏览器的驱动  配套  下载配套的驱动
# 放在appium安装包下
# 把旧版本保存下来，把新版本放进去
# 3.在d盘新建一个目录，把chrome驱动放进去就行了

# 进入H5页面 打印进入的h5页面
# contexts = driver.contexts
# print(contexts)
# # 打印出的内容放到切换的内容中去
#
# # 切换到h5页面
# driver.switch_to.context('WEBVIEW_com.tencent.edu')
# print('已经进入到内嵌网页7')