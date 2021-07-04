'''
@author:lvming
@time:2021/6/27
'''
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

'''
    基类:pom体系下的底层代码，用于封装各类行为操作，便于页面对象类进行调用。
	    根本核心是关键字驱动设计理念。
	    
'''
# 基类
class BasePage:
    # 定义常规的测试操作行为
    # 创建一个临时driver对象，便于代码的编写。
    # driver = webdriver.Chrome()
    # 构造函数：用户初始化self.driver对象。要考虑到driver对象可能是任意的一种浏览器对象。
    def __init__(self,driver):
        self.driver = driver
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self, txt):
        self.driver.get(txt)

    # 关闭释放资源
    def quit(self):
        self.driver.quit()

    # 元素定位:目的是为了通过一个方法实现所有的元素定位。
    # 如果不return，就无法获得你定位的元素对象，在后续执行输入这一类操作的时候就会报错。
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 对于元素定位，如果有复数，该怎么办。复数的定位很少用到。只有在特定场景下才会有，所以可以先不管。
    # 复数定位
    def locator_s(self):
        pass

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    # wk.click(name='link text',value='登录')
    def click(self, loc):
        self.locator(loc).click()

    # 强制等待
    def sleep(self, txt):
        sleep(txt)

    # 显式等待
    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(loc), message='等待元素失败')

    # 文本断言
    def assert_text(self, loc, txt):
        try:
            assert txt == self.locator(loc).text, '断言失败'
            return True
        except:
            return False
