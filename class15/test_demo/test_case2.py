'''
@author:lvming
@time:2021/7/3
'''
'''
    pytest中用例的管理手段：mark
    可以通过mark装饰器对所有的用例进行标记，不同的标记区分进行管理
'''
import pytest

@pytest.mark.webui
def test_01():
    print('web01')

@pytest.mark.webui
@pytest.mark.temp
def test_02():
    print('web02')

@pytest.mark.interface
@pytest.mark.temp
def test_03():
    print('interface01')

@pytest.mark.interface
def test_04():
    print('interface02')

if __name__ == '__main__':
    # pytest.main(['-s','test_case2.py','-m webui'])
    # pytest.main(['-sv','-m webui or interface'])
    pytest.main()
    # pytest -s -m "temp or interface"