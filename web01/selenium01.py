'''
@author:lvming
@time:2021/6/22
'''


'''
Selenium（js为核心的技术）:
目前有4个版本
（1、seleniumIDE的应用，基于FireFox浏览器的插件
2、WebDriver+SeleniumIDE
3、是目前主流版本，摒弃了SeleniumIDE，完全基于WebDriver来实现
4、Alpha版本，不推荐。）
除了SeleniumIDE存在之外，还有SeleniumGrid，自动化测试的分布式部署模块，
除去单独应该用在测试框架的部署之外，还可以结合Jenkins实现自动化持续继承的分布式部署。
'''
# Selenium核心组件：
# WebDriver+SeleniumIDE(不用)+SeleniumGrid
# 环境部署：
#    1.安装Python环境
#    2.安装Selenium：pip install selenium
# pip指令因为源的链接问题，可能会出现有超时的异常。解决办法是添加—default-timeout=1000
# 也可以选择切换到国内源的方式来安装，但是国内源有一些模块是没有的。
# Selenium就是基于WebDriver来实现的。
# WebDriver：
#    在python的selenium模块中，是一个子模块。本质意义上分为两个部分。一是子模块，二是一个服务（也是一个exe文件）
#    环境安装：
# 	1.检查自己的浏览器：
# 	   支持的浏览器参照selenium官网
# 	2.以chrome浏览器为例：
# 	   1.下载对应浏览器版本的chromedriver
# 	   2.解压webdriver，将chromedriver.exe文件解压到python的安装路径下。
# Webdriver本质意义上是一个服务器，是一个基于HTTP网络协议进行交互的服务(俗称代理),用于接收和处理两段的信息内容
#导入selenium模块
from selenium import webdriver
from time import time, sleep

# 启动浏览器:浏览器的首字母要大写,还要添加()
driver=webdriver.Chrome()
# 访问url:一定要在url中添加http://这样的内容,如果不加会报错,必须加//
driver.get('http://www.baidu.com')
# 输入秋水好蠢 通过find element函数查找元素，一定是查找有对应属性的元素
driver.find_element_by_name('wd').send_keys('秋水好蠢')
# 点击'百度一下'按钮实现搜索
driver.find_element_by_id('su').click()
#添加等待
sleep(3)
#关闭浏览器
driver.quit()
