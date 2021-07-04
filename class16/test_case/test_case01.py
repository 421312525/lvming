'''
@author:lvming
@time:2021/7/3
'''
'''
    课程回顾：
       1.Pytest环境部署
       2.Pytest运行机制以及配置文件
    Pytest指令详解：
       1.数据驱动 pytest装饰器@pytest.mark.parametrize
       所有的数据都会最终成为一个list的格式来传递到用例当中
       2.多线程用例并发插件：
        pip install pytest-xdist
       3.用例失败重新运行机制
       pip install pytest-rerunfailures
        —lf：只运行上一次失败的测试用例
        —ff：先运行上一次失败的测试用例，再运行其它所有测试用例
        
        Allure测试报告：
           第一步：要搭建java环境才可以运行allure,也就是jdk1.8
           第二步：解压allure压缩包
           第三部：配置allure\bin到环境变量
           allure测试报告是基于pytest运行后，生成的json文件，来实现的结果展示，以一个工程的形态展示本次的所有测试结果
           要集成pytest实现allure的展示，需要安装：
           pip install allure-pytest   
           pytest -s test_case03.py --alluredir ./result/
           allure generate ./result/ -o ./report_allure
                pytest.main(['allure generate ./result/ -o ./report_allure --clean'])

'''
import pytest
from class16.data_driver.yaml_driver import load_yaml
import requests

token = None
# 需要数据的测试用例:数据驱动可以直接传递数值，也可以通过函数的形式将结果生成并返回。
# @pytest.mark.parametrize(['user','password'],[('admin','123456'),('admin1','')])
# def test_login(user,password):
#     print('--------------')
#     print(user)
#     print(password)

@pytest.mark.parametrize('data',load_yaml('../data/user.yaml'))
def test_login(data):
    # print('--------------')
    # print(data)
    url = 'http://39.98.138.157:5000/api/login'
    res = requests.post(url=url,json=data)
    # print(res.text)
    global token
    token = res.json()['token']
    # print(token)

def test_02(xuzhu01):
    print('test02')
    print(xuzhu01)
    headers = {
        'token':xuzhu01
    }

if __name__ == '__main__':
    pytest.main(['-s'])