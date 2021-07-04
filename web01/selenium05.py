'''
@author:lvming
@time:2021/6/23
'''
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

'''
课程回顾：
   1.常规元素操作，iframe和句柄的切换。
   2.注册电商系统账号，实现自动化注册与登录流程。
	作业问题：
	   1.很多同学，听了课和没听课是一样的
	   2.copy xpath会有问题的。
	   3.By对象实现元素定位有问题嘛？
	   4.数据分离文件。所有被分离的元素在定义和声明的时候是常量。常量是大写的。不是小写的。
	   5.断言。有点勉强，在UI的阶段下断言只是为了校验最后的结果。
'''
# 等待的用途：
#    自动化测试是基于机器来实现的测试行为，本质意义上还是点点点的行为操作。在运行测试的代码时经常会因为代码的问题导致运行时失败。
#    自动化测试首先要求的是成功率，也就是稳定性。
#    自动化测试流程的稳定性需要通过等待来保障。代码不需要考虑运行时间，但是代码运行的对象要考虑时间。

# 三类等待：
'''
# 1.强制等待
    不考虑整体代码的连贯性和逻辑性，运行到强制等待时，就直接停止指定的时间，时间结束后，再继续运行后面的代码
    sleep表示强制等待，以秒为时间单位，是在time包下的类
    优势：容易上手。有需要的时候直接调用即可。对于新手特别友好
    劣势：迟钝。在自动化执行时会造成大量的时间浪费。
    一般而言都是新手在使用sleep，或者是临时性的调试应用。或者特定情况。
# 2.隐式等待
    悄悄的等待。本质意义上而言是driver的一个设置项。
    只需要设置一次，即可在driver的整个生命周期中生效
    隐式等待的时间也是基于秒来进行等待的。但是隐式等待会在找到元素后直接结束
    如果没有找到元素，就会等到设置的最大时间,等待的过程中一直会寻找这个元素
    如果最终没有找到元素，就继续运行下一行代码。
    隐式等待必须要等待页面加载完成之后再生效。所以效率的提升不是太明显。
    没有办法指定到元素来进行等待。
    一般而言隐式等待都会添加。添加的时间一般是5秒或者10秒
    优势：在整个webdriver声明周期中，只需要设置一次即可。
# 3.显式等待
    专门针对元素来进行等待的。
    和强制等待一样，在需要调用的时候就要定义。
    显式等待分为until和until_not两种函数来实现等待，作用是完全相反的
    如果元素未找到，会抛出timeout的异常。
    显式等待在执行的时候会有一个return.返回等待的元素
    优势：可以直接对单个元素进行等待，效率最高。
    劣势：代码太长了，用起来比较麻烦。
    显式等待还可以当做断言的形式来使用。
在实际的自动化测试中，等待是综合运用的。
当显示与隐式同时存在的时候：
	1.如果显示等待的元素找不到，则抛出超时异常。
	2.基于两者等待机制的时间设定，默认遵循时间更长的等待。
弹窗机制：
	很久没用过了。现在的系统很少有了。因为所有的弹窗交互都是基于div层直接实现。
	所有形式的弹窗不是页面弹出，二十浏览器弹出。
	在浏览器中有三类弹窗：
	   1.alert：确认
	   2.prompt：支持输入并确定
	   3.confirm：确定与 取消
	   如果弹窗的样式与操作系统或者浏览器一个风格，则一定是alert
       如果弹窗的样式与软件系统一个风格，一般都是div层,只需要考虑是否存在iframe即可
'''

from selenium import webdriver

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.find_element('id','kw').send_keys('虚竹')
driver.find_element('id','su').click()
# 强制等待
# sleep(2)
# 显式等待
el = WebDriverWait(driver,5,0.5).until(
    lambda el1:driver.find_element('xpath','//*[@id="1"]/h3/a'),
    message='元素查找失败')
el.click()
# WebDriverWait(driver,5,0.5).until_not(
#     lambda el:driver.find_element('xpath','//*[@id="1"]/h3/a'),
#     message='元素查找失败')
# driver.find_element('xpath','//*[@id="1"]/h3/a').click()
# driver.find_element('xpath','//*[@id="1"]/h3/a').click()
print('这是a1元素后的代码')
driver.quit()

#alert弹窗处理
alert = driver.switch_to.alert()
alert.accept()
#confirm弹窗处理
alert.accept()
alert.dismiss()
#prompt
alert.sendkeys()
alert.accept()
alert.dismiss()
#获取alert弹窗的文本
alert = alert.text
# 课后作业：
#   通过自动化测试行为，实现电商的下单流程。
# 	登录-搜索商品-添加商品属性-加入购物车-校验购物车是否添加成功
#   iphone6
