'''
@author:lvming
@time:2021/6/24
'''
from selenium.webdriver import ActionChains

'''
鼠标悬停：mouse_hover
通过ActionChains类来实现悬停的操作行为。
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('http://www.baidu.com')
el = driver.find_element('xpath','//span[text()="设置"]')
# 创建actions对象，进行悬停的操作,固定写法,在悬停的时候，鼠标不要乱动。避免出现问题
actions = ActionChains(driver)
actions.move_to_element(el).perform()
driver.find_element('link text','搜索设置').click()
# 很多系统里会出现有报错，提示元素无法进行click交互
# 通过webdriver创建的浏览器对象，默认是零缓存对象，也就意味着所有之前所缓存的内容，在这个对象中，都不存在。启动时不会加载本地缓存。
# 截图:自己写路径进行文件保存
driver.save_screenshot('/Users/v_lvming/Downloads/1.png')

# 验证码的处理：
# 在自动化中非常常见的场景就是验证码的处理。
# 如果测试的时候遇到验证码。就直接找开发要万能验证码输入即可，或者找开发屏蔽验证码，解决验证码的问题。
# 因为验证码的存在本身就是用来防止机器操作的。
# 如果再在要运行验证码，建议是在执行的时候预留等待时间，通过手动操作来实现。