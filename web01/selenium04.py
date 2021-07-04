'''
@author:lvming
@time:2021/6/23
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

'''
课程回顾：
   1.八大元素定位法则：
	PS：在定位元素的时候，如果对于元素的定位不自信或者担心会不准确，可以通过开发者工具的筛选功能来校验元素的定位正确性。
   2.课后作业：
     实现网易云音乐web端的自动化第三方QQ登录操作。
       1.元素定位的函数。
	      find element by xxx的定位方法其本质是调用的find element函数，在实际应用中，通过by xxx的定位方法进行定位的实际操作其实不多。主要都是使用的find element函数来实现元素定位
	   2.句柄的切换，喜欢用-1来定位到第二个句柄，这种方式不太推荐
	   3.断言：
        自定义函数，查找元素是否显示。（这个行为在selenium库中有线程的函数。不需要自定义。）
        获取title，来判断是否成功。（很多时候因为网络，页面无法在短时间内显示，但是title很容易显示）
       4.变量或者函数，命名的时候用拼音是不允许的。
'''
from selenium import webdriver

driver = webdriver.Chrome()

# 窗体最大化:有部分元素需要在窗体最大化的时候才可以执行操作。
# 元素无法正常交互的异常：一般是因为当前展示的页面内容无法查找到这个元素，所以抛出异常
driver.maximize_window()

# driver.get('http://pic.baidu.com/')
#
# driver.find_element('xpath','//*[@id="sttb"]/img[1]').click()
# # 上传文件时输入的是文件的路径
# driver.find_element('xpath','//input[@id="stfile"]').send_keys(r'/Users/v_lvming/Downloads/lvming.png')

# 访问url
driver.get('http://39.98.138.157/shopxo/index.php')

# 点击操作:无所谓是什么元素，只要是需要执行点击操作，都可以调用click
driver.find_element('xpath','//a[text()="登录"]').click()

# 输入：只有input标签才可以实现sendkeys的输入，文本域textarea貌似也可以(很不常见)
driver.find_element('name','accounts').send_keys('xuzhu666')
# 文件上传，也可以使用sendkeys，但是，仅限于input标签，如果是非input标签的文件上传，请使用autoIT

# 账号密码的输入都是sendkeys，因为这些文本框都是input标签。
driver.find_element('name','pwd').send_keys('123456')

# 点击登录
driver.find_element('xpath','//button[text()="登录"]').click()

# 下拉列表框:一般都是基于input或者div来实现的。样式是下拉列表框的样式，但本质上不是下拉列表框
# 正统的下拉列表框是select标签，一般顶层是select，选项是options
'''
div下拉列表框，通过两次点击来获取你想要的值
input下拉列表框：
	1.通过两次点击来获取值(最稳妥的方式)
	2.通过修改readonly属性，再sendkeys输入值
select下拉列表框：
	1.定位select元素
	2.转成select对象
	3.基于下标、value、text三种方式来获取
'''
# 常规元素操作行为：
#    当你出现调用某个元素会报错的时候，考虑查看一下同级的其它元素，或者定位上级元素来尝试。
el = driver.find_element('name','schoolId')
select = Select(el)
# 获取所有的option内容
li = select.options
# 获取指定的值，进行传入
select.select_by_value('2913') #通过值
select.select_by_index(1) #通过下标
select.select_by_visible_text('北京八中固安分校') #通过文本

driver.quit()
#下一课是homework01