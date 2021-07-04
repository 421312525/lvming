'''
@author:lvming
@time:2021/7/2
'''
'''
    这是pytest中预置函数定义的配置文件:注意，文件名称一定是conftest.py，不能是其它的
    scope参数定义的4种等级（默认等级是function）：
    session：在本次session级别中只执行一次
    module：在模块级别中只执行一次
    class：在类级别中只执行一次
    function：在函数级别中执行，每有一个函数就执行一次
'''
import pytest

# 定义一个基本的setup和teardown
# @pytest.fixture(scope='session')
@pytest.fixture()
def xuzhu():
    print('虚竹是猪🐷')

@pytest.fixture()
def xuzhu01():
    return 1