'''
@author:lvming
@time:2021/7/3
'''
import pytest
import requests
from class16.data_driver.yaml_driver import load_yaml


@pytest.fixture()
def xuzhu01():
    url = 'http://39.98.138.157:5000/api/login'
    data = {
        'username':'admin',
        'password':'123456'
    }
    res = requests.post(url=url, json=data)
    print(res.text)
    token = res.json()['token']
    return token