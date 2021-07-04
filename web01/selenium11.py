'''
@author:lvming
@time:2021/6/25
'''
# 关键字驱动类 *****


'''
课程回顾：
1.ChromeOptions配置
2.ui自动化实操
作业问题：
   1.喜欢try except(是这段代码可能会出现问题，单位了不影响后续代码的正常运行，所以将异常抛出，保证完整性)。
   2.喜欢做莫名奇妙的if判断。
   3.喜欢做看起来很专业的封装，但实际并没有什么用。
   4.加载了本地缓存，为什么电商系统还是需要登录?
    加载本地缓存≠免登陆

关键字驱动：
   测试框架下最为核心的设计模式。
   在软件测试领域下，关键字驱动是目前而言最为基本的框架设计模式，同时也是最为核心的框架设计模式。
   其实本质上就是面向对象编程。类和函数的封装。
   在市场中主流的测试工具基本都是基于关键字驱动来实现的。
   对于selenium而言，本身是具备有非常完整的一个自动化测试封装体系。对于实际的自动化测试而言，我们用不了这么多东西。而且还是基于selenium本身的语法来进行应用。
   selenium本身的线性代码的实现，在维护上是非常麻烦的。
   在线性代码的实现上，代码的冗余是非常多的。
   线性代码是无法实现团队协作模式。
   在阅读上是非常糟糕。
   所以线性代码的实现，本质意义上是为了学习和熟悉selenium而进行的。
   为了让代码可以在实际企业中正常应用。所以需要用业内通用的设计模式来完成结构的设计。
   关键字驱动：基于指定的关键字来对应不同的操作行为。
   问题：
   webdriver对象与自定义的封装类对象有区别吗？
   是完全不同的两个东西
'''
'''
关键字驱动
    selenium就是一个大商场。
    按照自己的需要去买需要的东西。因为只有自己需要的东西才会有价值。
所以将selenium中我们需要的内容进行提取，带回家，变成对自己有假肢的内容。
关键字驱动就是很多人口中所谓的selenium的二次封装。
常用的selenium操作行为：
   1.元素定位
   2.输入
   3.点击
   4.关闭
   5.等待
   6.切换句柄
   7.访问url
   8.创建webderver对象
在封装selenium的时候，只要自己要的。
在初期封装完成的关键字驱动类，可以依照自己最初的定义去封装，如果发现有内容无法基于先有类满足，就继续添加新的关键字即可。
关键字驱动类的实现：
   1.结构设计：
      工程结构上一定要注意到逻辑代码与测试代码的分离。
	逻辑代码：为测试代码提供服务的，本身不执行任何的测试操作行为。
	测试代码：可以理解为测试用例
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from web01.options import Options
from time import sleep
#在后续的自动化中通过调用这个类，来实现selenium操作：逻辑代码

# 要满足创建任意一个浏览器对象的需求。
# 不同的driver初始化形式，自己挑喜欢的
def open_browser(type_):
    # 基于反射的形态来简化代码
    try:
        driver = getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome(options=Options().conf_options())
    return driver
    # try:
    #     if type_ == 'Chrome':
    #         return webdriver.Chrome(options=Options().conf_options())
    #     else:
    #         return getattr(webdriver,type_)()
    # except:
    #     return webdriver.Chrome()
class DriverKey:
    # 定义常规的测试操作行为
    # 创建一个临时driver对象，便于代码的编写。
    # driver = webdriver.Chrome()
    # 构造函数：用户初始化self.driver对象。要考虑到driver对象可能是任意的一种浏览器对象。
    def __init__(self,txt):
        self.driver = open_browser(txt)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self,txt):
        self.driver.get(txt)

    # 关闭释放资源
    def quit(self):
        self.driver.quit()

    # 元素定位:目的是为了通过一个方法实现所有的元素定位。
    # 如果不return，就无法获得你定位的元素对象，在后续执行输入这一类操作的时候就会报错。
    def locator(self,name,value):
        return self.driver.find_element(name,value)

    # 对于元素定位，如果有复数，该怎么办。复数的定位很少用到。只有在特定场景下才会有，所以可以先不管。
    # 复数定位
    def locator_s(self):
        pass

    # 输入
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    # 点击
    # wk.click(name='link text',value='登录')
    def click(self,name,value):
        self.locator(name,value).click()

    # 强制等待
    def sleep(self,txt):
        sleep(txt)

    # 显式等待
    def wait(self,name,value):
        WebDriverWait(self.driver,10,0.5).until(lambda el:self.locator(name,value),message='等待元素失败')

    # 隐式等待 不需要封装，一般而言隐式是配置，是固定的等待时间。
    # 句柄切换，包含关闭原页面
    # 句柄切换，不包含关闭原页面
    # 文本断言
    def assert_text(self,name,value,txt):
        try:
            assert txt == self.locator(name,value).text,'断言失败'
            return True
        except:
            return False


    # 关键字驱动拓展：
    #    1.基于操作行为实现的关键字驱动，是相对通用型的测试逻辑
    #    2.基于业务流程实现的关键字驱动封装，类似于后续所讲POM。
    # 	将常用的固定业务封装为关键字，通过关键字的调用来实现流程的简化。
    #    基于业务逻辑封装的关键字，不是那么好用。一般只提取部分共用的内容进行封装。
    #    复用性只能够基于当下系统来实现。
    #    其实是推荐POM的形态来实现。
    # 课后作业：
    #    1.自行封装自己的关键字驱动类
    #    2.通过自己的关键字类实现原有的添加购物车流程与修改个人资料流程。
    #    3.可以加入上节课所实现的ChromeOptions配置。