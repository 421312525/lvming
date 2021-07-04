'''
@author:lvming
@time:2021/6/24
'''
from time import sleep

'''
Document对象，是前端中的顶梁柱。UI自动化的过程中操作的就是前端对象，对于一些特殊场景，可以通过document对象来进行处理。
作用：
	1.定位元素
	2.通过Document
	3.滚动条操作:目前要么可以忽略，要么只能通过js来实现。
	滚动的比例记3个数值：
        1. 0 表示最上方
        2. 500 表示中间
        3. 1000 表示末尾
	4.滚动到指定元素
	操作滚动条的目的就是为了将制定的元素显示出来，能够通过selenium进行定位与操作。
	
document.getElementById('kw')
添加属性
document.getElementById('kw').setAttribute('lvming','真棒')
移除属性
document.getElementById('kw').removeAttribute('lvming')

滚动操作
    window.scrollTo(0,500)  x左右滚动，y上下滚动
    操作滚动条的目的就是为了将制定的元素显示出来，能够通过selenium进行定位与操作。
'''
from selenium import webdriver


# 启动浏览器:浏览器的首字母要大写,还要添加()
driver=webdriver.Chrome()
driver.maximize_window()
# 访问url:一定要在url中添加http://这样的内容,如果不加会报错,必须加//
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
# 输入秋水好蠢 通过find element函数查找元素，一定是查找有对应属性的元素
# driver.find_element_by_name('wd').send_keys('虚竹')
# # 点击'百度一下'按钮实现搜索
# driver.find_element_by_id('su').click()
# #添加等待
# sleep(3)

# el = driver.find_element('xpath','//*[@id="1"]/h3/a')
# 滚动条操作js语句
# js = 'window.scrollTo(0,1000)'
# 通过js执行器来实现js语句的调用。
# driver.execute_script(js)
# sleep(3)

# el = driver.find_element('xpath','//*[@id="1"]/h3/a')
# js精准定位到制定元素，并显示
# js = 'arguments[0].scrollIntoView()'
# el = driver.find_element('xpath','//*[@id="kw"]')
# js = 'arguments[0].removeAttribute("name")'
# 调用js执行器
# driver.execute_script(js,el)

el = driver.find_element('xpath','//*[@id="s-top-left"]/a[1]')
# 通过js获取对象或者内容时，需要在原有的js语句上添加return
js = 'return arguments[0].innerHTML'
text = driver.execute_script(js,el)
print(text)

#关闭浏览器
# driver.quit()

# 课后作业：
# 1.将原有的电商添加购物车流程添加断言
# 2.实现从登录到个人中心用户信息修改整个流程，包含头像上传，结合断言完善整个自动化流程。