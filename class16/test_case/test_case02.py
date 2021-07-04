'''
@author:lvming
@time:2021/7/3
'''
from time import sleep

import pytest
from selenium import webdriver


def test_01():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    sleep(2)
    driver.quit()

def test_02():
    driver = webdriver.Chrome()
    driver.get('http://www.bilibili.com')
    sleep(2)
    driver.quit()

def test_03():
    driver = webdriver.Chrome()
    driver.get('http://www.douyu.com')
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    pytest.main(['test_case02.py','-n','3'])