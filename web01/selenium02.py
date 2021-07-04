'''
@author:lvming
@time:2021/6/22
'''
# 从webdriver模块的底层代码应用来了解selenium+webdriver对浏览器进行交互的全过程
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

# # 启动浏览器:浏览器的首字母要大写,还要添加()
# driver=webdriver.Chrome()
wd=WebDriver(executable_path='chromedriver')
# # 访问url:一定要在url中添加http://这样的内容,如果不加会报错,必须加//
# driver.get('http://www.baidu.com')
wd.execute('get', {'url': 'http://www.baidu.com'})
# # 输入秋水好蠢 通过find element函数查找元素，一定是查找有对应属性的元素
# driver.find_element_by_name('wd').send_keys('秋水好蠢')
el=wd.execute('findElement', {
            'using':'xpath',
            'value':'//input[@id="kw"]'})['value']
print(type(el))
el._execute('sendKeysToElement',{
    'text':'今天天气怎么样',
    'value':''
})
# el=wd.execute('clickElement')['value']
# # 点击'百度一下'按钮实现搜索
# driver.find_element_by_id('su').click()
# #添加等待
sleep(3)
# #关闭浏览器
# driver.quit()
wd.execute('quit')

