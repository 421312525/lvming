'''
@author:lvming
@time:2021/6/24
'''
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from web01.options import Options

'''
    1.实现商品添加的流程自动化
        复制选中的行数，默认是一行，ctrl+d
        对于一些重复的代码能cv就cv
    
'''
from selenium import webdriver

# 添加的商品数量
number = '4'
# 启动浏览器
driver = webdriver.Chrome(options=Options().conf_options())
# 隐式等待
driver.implicitly_wait(10)
# 获取网址
driver.get('http://39.98.138.157/shopxo/index.php')
# 登录操作
driver.find_element('link text','登录').click()
driver.find_element('name','accounts').send_keys('xuzhu666')
driver.find_element('name','pwd').send_keys('123456')
driver.find_element('xpath','//button[text()="登录"]').click()
# 搜索手机商品
driver.find_element('id','search-input').send_keys('手机')
driver.find_element('id','ai-topsearch').click()
driver.find_element('xpath','//div[@class="items"]/a[1]').click()
# 切换到商品详情页
handles = driver.window_handles
driver.close()
driver.switch_to.window(handles[1])
# 添加商品属性 建议请添加强制等待
driver.find_element('xpath','//li[@data-value="套餐一"]').click()
driver.find_element('xpath','//li[@data-value="金色"]').click()
driver.find_element('xpath','//li[@data-value="128G"]').click()
sleep(1)
# 输入商品数量，先清空再输入
el = driver.find_element('xpath','//input[@id="text_box"]')
el.clear()
el.send_keys('4')
driver.find_element('xpath','//button[@title="加入购物车"]').click()
assert driver.find_element('xpath','//p[text()="加入成功"]').text=='加入成功','没有提示加入成功'
# sleep(3)
# 进入购物车页面 检查商品是否添加成功
sleep(2)
driver.find_element('xpath','//span[text()="购物车"]').click()
# handles = driver.window_handles
# driver.close()
# driver.switch_to.window(handles[1])
# 查看商品是否存在
WebDriverWait(driver,5,0.5).until(
    lambda el1:driver.find_element('xpath','//div[@class="goods-base"]/a[1]'),
    message='没有商品，添加失败')

# 校验添加的商品数量与预期是否一致 //input[@type="number"]
# driver.find_element('xpath','//input[@type="number"]')
assert driver.find_element('xpath','//input[@type="number"]').get_attribute("value") == number,'数量不是4'
driver.close()