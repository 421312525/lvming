'''
@author:lvming
@time:2021/6/20
'''
from class07.Demo02 import BasePage
from selenium import webdriver

driver=BasePage(webdriver.Chrome())
driver.open('http://www.baidu.com')
driver.on_input('id','kw','秋水')
driver.on_click('id','su')
driver.wait(3)
driver.on_click('xpath','//*[@id="1"]/h3/a/em')
driver.wait(3)
driver.close()