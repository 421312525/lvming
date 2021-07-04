'''
@author:lvming
@time:2021/6/23
'''


'''
课程回顾：
	1.三类等待、三类弹窗
	2.应用显式等待作为断言的机制。但是断言不要贪多。
	3.很喜欢用：
	   1.封装
	   2.for循环
	   3.if判断
	如果这个元素在，我就xxx，如果这个元素不在，我就ccc
	如果这个数据存在，我就aaa，如果这个数据不存在我就bbb
	这一类型的内容，在自动化中是不存在的。
	因为所有的自动化测试行为的执行，都是基于已知结果来进行的。
'''
'''
断言的机制：
   断言是自动化测试中，最为基本也是最为核心的内容。
   1.UI自动化中，断言是用来校验流程的正确性
   2.接口自动化中，断言是用来校验数据的正确性
   断言就是判断本次测试是否达到预期结果。
   在python中通过很多种方法都可以实现断言的效果。
   if else断言本质上的一种逻辑，常用的断言手段一般而言分为：
   1.assert在python中自带的关键字：基于表达式来进行断言
   2.显式等待,判断元素是否存在。
   3.通过if else，if则返回true,else则返回false
   断言只需要找到核心的内容，进行校验，就可以保证正确性。
   例如：
	进入一个系统，如果要走登录流程，校验是否登录成功的核心在于什么？
	1.提示登录成功！
	2.登录按钮不再显示在页面中
	3.一定会存在有退出
	4.一定会显示有登录成功后才可访问的功能
	提取一个关键信息进行断言即可。因为断言多了，除了多写几行代码，其它没有任何意义。
	
   断言本身就是用来校验正确性的，你如果把错误给处理了，你怎么知道对不对呢？
   断言本质上是预期结果与实际结果的匹配，那这个匹配当然是在最后再匹配的。
   在UI自动化中，断言是对流程的最终结果进行校验即可。中途可以通过显示等待做一些基本的校验，但是不推荐。
   自动化测试在一些特定情况下需要考虑到清理脏数据的操作。
   
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(5)
# 请求url
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
# 显式等待
el = WebDriverWait(driver,5,0.5).until(lambda el1:driver.find_element('name','accounts'),message='没有找到元素')
el.send_keys('xuzhu666')
# driver.find_element('name','accounts').send_keys('xuzhu666')
# 输入操作
driver.find_element('name','pwd').send_keys('123456')
# 点击操作
driver.find_element('xpath','//button[text()="登录"]').click()
# 强制等待
sleep(1)
# 获取退出按钮的文本
text = driver.find_element('link text','退出').text
# 校验文本是否符合预期结果
assert text == '退出','断言失败'