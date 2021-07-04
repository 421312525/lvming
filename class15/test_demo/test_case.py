'''
@author:lvming
@time:2021/7/2
'''
'''
    PyTest介绍：
   PyTest是一个测试用例的管理框架，在UnitTest基础上做的一个全面的升级。
   集成度更高，而且更加自由的一个测试框架，全称都是基于指令的形式来运行
    Pytest—UnitTest—RobotFramework—airtest
   Pytest环境部署：
       pip install pytest
       1.pytest默认规则是读取所有以test开头的文件
       2.fixture是pytest中的一大利器
       3.断言机制：assert
       4.pip install pytest-html 安装html测试报告  
       
        pytest --html=./report/report1.html --self-contained-html
       

'''
'''
    Pytest默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
    Pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
    多条指令一同运行时，需要空过空格进行区分，在main函数中，是通过，进行分割
    -v 用于详细显示日志信息
    -rA 测试结果的简单统计
    Pytest中的setup和teardown:一般可以用过一个配置文件直接进行管理：配置文件命名一定要是conftest.py
'''
import pytest

# 前置与后置
def setup_function():
    print('function')

def teardown_function():
    print('tfunction')

def setup_module():
    print('module')

def teardown_module():
    print('tmodule')

# 测试用例
@pytest.mark.webui
@pytest.mark.parametrize
def test_02(xuzhu):
    # print('test_02')
    assert xuzhu == 2,'失败'
def test_01(xuzhu01):
    # assert xuzhu01==1,'失败'
    print('test_01')

# pytest中class对象的定义：建议以test开头
# 类里面的没有执行setup和teardown
'''
    在class中前置后置函数的运行顺序：
        1.setup_class
        2.setup_,method
        3.setup
        4.teardown
        5.teardown_method
        6.teardown_class
'''
class TestDemo:
    def setup_class(self):
        print('setup_class')
    def teardown_class(self):
        print('teardown_class')
    def setup_method(self):
        print('setup_method')
    def teardown_method(self):
        print('teardown_method')

    def setup(self):
        print('inside setup')

    def teardown(self):
        print('inside teardown')

    def test_d1(self):
        print('testd1')

    def test_d2(self):
        print('testd2')

# pytest运行主入口
if __name__ == '__main__':
    # pytest.main(['-s'])
    # pytest.main(['-s','test_case.py::test_01','-v','-rA','-q'])
    pytest.main(['-s','-v','-rA','test_case.py'])

# 指定一条case执行 pytest -s test_case.py::test_02

# 课后作业：
# 1.部署pytest环境，自行熟悉
# 2.好好在看两边录播，多上上手
# 3.将原有的ui与接口测试框架，转型至pytest实现