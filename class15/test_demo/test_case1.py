'''
@author:lvming
@time:2021/7/2
'''
'''
    PyTest介绍：
   PyTest是一个测试用例的管理框架，在UnitTest基础上做的一个全面的升级。
   集成度更高，而且更加自由的一个测试框架，全称都是基于指令的形式来运行
   Pytest—UnitTest—RobotFramework—airtest

'''
'''
    Pytest默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
    Pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
    Pytest生成测试报告：pytest-html测试报告模块  pytest --html=./report/report.html --self-containted-html
    pytest-html测试报告模块，如果要集成到邮件，就需要添加指令—self-contained-html
'''
import pytest

# 测试用例
@pytest.mark.webui
def test_02():
    print('test1_02')

def test_01():
    print('test1_01')

# pytest运行主入口
if __name__ == '__main__':
    pytest.main(['-s'])