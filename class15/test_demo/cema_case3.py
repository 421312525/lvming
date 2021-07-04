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
def test_07():
    print('web07')

@pytest.mark.webui
@pytest.mark.temp
def test_08():
    print('web08')

@pytest.mark.interface
@pytest.mark.temp
def test_09():
    print('interface09')

@pytest.mark.interface
def test_10():
    print('interface10')

if __name__ == '__main__':
    # pytest.main(['-s','test_case2.py','-m webui'])
    pytest.main(['-sv','-m webui or interface'])
    # pytest -s -m "temp or interface"

# 配置文件中输入 python_files = cema*.py，只运行该文件下的