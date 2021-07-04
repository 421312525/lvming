'''
@author:lvming
@time:2021/6/27
'''
'''
    课程回顾：
   1.UnitTest的基础应用
   2.UnitTest下的全局变量的应用
   3.前后置条件的设定以及全局变量的应用
 	当你需要去查找为什么单独运行可以正常，但是在UnitTest中会报错，你可以选择建立一个新的测试用例，讲你需要的内容在新的用例中打印一下。

    UnitTest中的skip装饰器：
        用于管理测试用例的执行机制的。

    UnitTest中的skip装饰器应用:
       总共四种不同的skip装饰器：
        1.@unittest.skip：用例执行时，无条件跳过该条用例
        2.@unittest.skipIf():当if条件为真时，跳过操作
        3.@unittest.skipUnless:与skipIf为假时，当条件为假时，执行跳过
        4.@unittest.expectedFailure:当用例报错的时候，系统选择忽略掉它
'''

import unittest

from web01.selenium11 import DriverKey

# UnitTest类对象
class UnitDemo(unittest.TestCase):
    temp = 12


    # 测试用例2
    # @unittest.skipIf(temp is None,'跳过')
    def test_02(self):
        print('02')

    # 测试用例:测试执行内容,相当于是封装了一个函数。
    # @unittest.skip('无条件跳过该用例')
    def test_01(self):
        print('01')

    # 测试用例3
    # @unittest.skipUnless(1 == 2,'条件为假时跳过')
    def test_03(self):
        print('03')

    # 测试用例4
    # @unittest.expectedFailure
    def test_04(self):
        self.assertEqual(1,2,'断言失败')

# UnitTest的运行
if __name__ == '__main__':
    unittest.main()

