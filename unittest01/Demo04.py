'''
@author:lvming
@time:2021/6/27
'''
'''
    课程回顾：
       1.HTMLTestRunner测试报告和UnitTest中的套件与运行器
       2.所有的自动化测试归根结底都是编程技术的延伸。
       3.UnitTest与Excel，在课程体系内容中，这两者都是测试用例。
            如果要基于UnitTest来实现Excel数据驱动，那excel就只做测试数据的管理，不做操作行为的管理
    DDT：
       DataDriver Test,是一个自动化中应用特别常见的数据驱动模块，是一个完美契合UnitTest的模块。
       环境部署：
            pip install ddt
        UnitTest中的ddt数据驱动应用
            ddt模块所有的内容都是基于装饰器的形态来实现补充的
            一定要在调用ddt的类中声明ddt的调用，也就是在class前加入@ddt
            在需要调用数据驱动的用例前，调用@data，实现数据的驱动分离
    Yaml:
        Yaml是一种文件类型。后缀名为.yaml。
        可以在工程中作为配置文件或者数据驱动文件来调用。
        可以与UnitTest完美契合。
        环境部署
	        pip install PyYaml
	    yaml文件可以支持符合的数据类型进行统一管理。
        意味着不管是list，字典，还是各种嵌套格式，都可以完美支持,yaml是一种格式要求非常强迫症的文件格式
        dict格式中，： 才是完整的写法，必须要有空格
        file_data用于处理yaml格式的文件
        yaml格式的数据驱动管理是一个yaml对应一条用例。
'''
# 基于ddt来实现的UnitTest的数据驱动形态。

import unittest
from ddt import ddt,data,unpack,file_data
from web01.selenium11 import DriverKey

# 文件的内容读取
def read_file():
    li = []
    file = open('./Demo04_data/data.txt','r',encoding='utf-8')
    for line in file.readlines():
        li.append(line)
    return li
# UnitTest类对象
@ddt # 声明该class类将要调用ddt模块进行数据管理。
class UnitDemo(unittest.TestCase):
    # 预置函数
    def setUp(self) -> None:
        self.wk=DriverKey('Chrome')
    # 后置函数
    def tearDown(self) -> None:
        self.wk.quit()

    # 测试用例1
    '''
        data执行的操作就是拆包
            @data('虚竹嘛','做人嘛，最重要的就是开心','狐狸是个留级生')
            将所有的数据以逗号进行分割:
                虚竹
                做人
                狐狸
            基于拆分出来的结果总数，定义循环次数，每次循环都传入一个参数进去
            ('http://www.jd.com','虚竹嘛')=*args
        当需要传入多个参数的时候，所以需要二次解包
    '''
    # 元组、列表、字典都可以作为参数的传入类型
    # @data(('http://www.jd.com','虚竹嘛'),('http://www.jd.com','做人嘛'),('http://www.jd.com','狐狸'))
    # @data([('http://www.jd.com','虚竹嘛'),('http://www.jd.com','做人嘛')])
    # @data({'url':'http://www.jd.com','name':'xuzhu'})
    # @data(('http://www.jd.com','虚竹嘛'),
    #       ('http://www.jd.com','做人嘛'),
    #       ('http://www.jd.com','狐狸'))
    # @unpack
    # def test_01(self,url,name):
    #     self.wk.visit(url)
    #     self.wk.input('id','key',name)
    #     self.wk.click('xpath','//button[@aria-label="搜索"]')
    #     self.wk.sleep(3)

    # 基于文件的内容读取,实现数据驱动:本质意义上是调用的函数的返回值，进行操作，而文件操作本身是在函数中进行的.
    # 测试用例2
    # @data(*read_file())
    # def test_02(self,name):
    #     print(name)
        # self.wk.visit('http://www.jd.com')
        # self.wk.input('id','key','手机')
        # self.wk.click('xpath','//button[@aria-label="搜索"]')
        # self.wk.sleep(3)
    #
    # # 测试用例3
    # def test_03(self):
    #     li = read_file()
    #     print(li)

    # 测试用例
    '''
        通过file_data读取的所有内容，传入kwargs参数
    '''
    @file_data('./Demo04_data/test_data.yaml')
    def test_01(self,**kwargs):
        self.wk.visit(kwargs['url'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(3)

    # @file_data('./Demo04_data/test_data1.yaml')
    # def test_01(self,url,txt):
    #     self.wk.visit(url)
    #     self.wk.input('id','key',txt)
    #     self.wk.click('xpath','//button[@aria-label="搜索"]')
    #     self.wk.sleep(3)
# UnitTest的运行
if __name__ == '__main__':
    unittest.main()

#    课后作业：
#    将原有UnitTest实现的自动化测试流程，基于Yaml来实现数据的管理