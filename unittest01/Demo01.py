#!/usr/bin/env python3
'''
@author:lvming
@time:2021/6/27
'''
'''
UnitTest测试框架：
   本质意义上而言是一个用例的管理框架。
   UnitTest是目前业内主流的自动化测试框架之一。市场现在主要进行用例管理的测试代码基本上都是基于UnitTest/PyTest来实现的。主要是用于接口的管理用例。因为确实很简单。
   环境的搭建：
	啥都不用干。因为UnitTest是默认安装的官方库。直接调用就可以了。
   四大特色：
	1.良好的测试用例管理机制。所有UnitTest中的测试用例都是基于固定的格式来实现的。UnitTest.TestCase来实现的。
	2.套件与运行器，专门用于管理测试用例以及运行测试用例后生成测试报告的模块。
	3.setup与teardown，前置与后置条件。
	4.断言机制。所有的断言行为都已经封装在UnitTest中，直接通过调用self.就可以把断言给点出来。
	如果自主封装有断言的函数，在UnitTest中直接调用，即便断言失败，测试用例还是通过。

    UnitTest测试框架的实操Demo语法规则讲解：
        1.如果要UnitTest生效，需要让自定义类直接继承UnitTest.Testcase类
        2.Unittest中测试用例都是以函数的形式存在,同时命名需要以test开头，推荐使用test_开头
        3.测试用例运行一定要在类中调用main，再在main中调用unittest.main()
            如果不写main方法，则类中会默认调用main方法，但是，为了格式规范，一定要写出来
        4.在类中基于编译器可以单独运行测试用例，但是不要用，因为容易报错
        5.如果我不以test开头命名函数，请问，这是什么东西。就是普通函数，用于被测试用例去调用的。
        6.测试用例的执行顺序，在UnitTest中是有默认的执行顺序的，这个顺序无法被轻易改变
            0-9,A-Z,a-z是默认顺序，排序规则是依照ASCII码排序规则
        7.在unittest中，用例运行后。默认是会强制关闭并结束进程。但是也会出现部分不清空的情况
            所以第一，不要考虑如果在用例执行后不关闭浏览器；第二，记得在用例末尾添加quit函数，确保资源的释放
        8.前置与后置是固定写法，所有的前置后置都是有且最多只能有一个
        9.用例执行前都会运行一次setup,执行后都会运行一次teardown
        10.所有的前置与后置不参与到实际的测试行为，只做初始化与资源释放的操作。
        11.对于前置条件不统一的情况，用万能setuo和teardown，或者是通过管理手段（分成多个py文件实现）
        12.class级别的setup和teardpwn需要通过装饰器@classmethod进行声明
        13.class级别的前后置通过cls定义类成员。但是是通过self来调用
        14.UnitTest中的断言应用
'''
# 导入UnitTest环境
import unittest
from web01.selenium11 import DriverKey

'''
类文件执行顺序：
	1.main
	2.继承于UnitTest.TestCase类的class
	3.setupClass(一个class对象只执行一次)
	4.setup(每个测试用例都执行一次)
	5.测试用例
	6.testdown(每个测试用例都执行一次)
	7.teardownClass(一个class对象只执行一次)
'''
# UnitTest类对象
# class UnitDemo(unittest.TestCase):
#     temp = 'xuzhu'
#     # 类前置:作用域只有当前class
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.wk = DriverKey('Chrome')
#     # 类后置:作用域只有当前class
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.wk.quit()
#
#     # 前置-> None 表示返回None,也就是没有返回结果的意思。其实就是不用管它
#     def setUp(self):
#         # self.wk = DriverKey('Chrome')
#         # self.wk.visit('http://
#         pass
#     # 后置
#     def tearDown(self):
#         # self.wk.click('id', 'su')
#         # self.wk.sleep(3)
#         pass
#         # self.wk.quit()
#
#     # 测试用例:测试执行内容,相当于是封装了一个函数。
#     def test_01(self):
#         # print('zhuzhuzhu')
#         # print('01')
#         # wk = DriverKey('Chrome')
#         self.wk.visit('http://www.baidu.com')
#         self.wk.input('id', 'kw', '笔记本')
#         self.wk.click('id', 'su')
#         self.wk.sleep(3)
#         # wk.quit()
#     # 测试用例2
#     def test_02(self):
#         # print('02')
#         self.xuzhu()
#         # wk = DriverKey('Chrome')
#         self.wk.visit('http://www.baidu.com')
#         self.wk.input('id', 'kw', '手机')
#         self.wk.click('id', 'su')
#         self.wk.sleep(3)
#         print(self.temp)
#         # wk.quit()
#     # 测试用例3:这个写法错了
#     def test_03(self):
#         self.wk.input('id', 'kw', '平板电脑')
#
#     # 函数:被调用就生效，不调用就是废代码
#     def xuzhu(self):
#         print('zhuzhuzhu')

# 这两种不是以test开头，所以不是测试用例
    # def atest(self):
    #     print('a')
    #
    # def b_test(self):
    #     print('b')

# unittest中关于全局变量的定义与修改与调用
class UnitDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = 'xuzhu'

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_01(self):
        print('01')
        # 调用temp变量
        print(self.temp)
        # self的赋值方式是用于在当前函数中改变变量的值，进队函数内有效
        # self.temp = '123' + self.temp
        # 类名的赋值方式是用于在class中改变变量的值，在函数外依旧有效。
        UnitDemo2.temp = 'ssss' + self.temp
        # UnitDemo2.temp = None
        print(self.temp)
        # 断言的调用
        # self.assertEqual(self.temp,'xuzhu','断言失败') # 和 == 一样,表示两者是否一样
        # 这样才是我们自己的关键字驱动封装下，UnitTest中完整的断言机制。
        # status = self.wk.assert_text()
        # self.assertTrue(status,msg='断言失败') # 判断内容是否为True
        # self.assertEqual()
        # self.assertEquals()
    def test_02(self):
        print('02')
        print(self.temp)
        # self.assertEqual(self.temp,'xuzhu','断言失败')

# UnitTest的运行
if __name__ == '__main__':
    unittest.main()

#    课后作业：
#    1.将关键字驱动类封装的内容，基于数据驱动实现的测试流程转换为UnitTest下的实现流程。