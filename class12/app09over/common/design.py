'''
@author:lvming
@time:2021/6/29
'''
# 先拿到配置文件的值
from time import sleep

import yaml
from appium import webdriver
def appium_yaml_conf():
    # 拿yaml文件 ../config/desired_caps.yaml
    with open('../config/desired_caps.yaml') as f:
        # 拿yaml文件的数据
        data = yaml.load(f,yaml.FullLoader)
        print(data)

    # 拿到数据之后，放在配置参数里面
    info = {}
    info['platformName'] = data['platformName']
    info['platformVersion'] = data['platformVersion']
    info['deviceName'] = data['deviceName']
    info['appPackage'] = data['appPackage']
    info['appActivity'] = data['appActivity']
    info['noReset'] = data['noReset']

    # driver = webdriver.Remote()
    driver = webdriver.Remote('http://'+data['ip']+':'+str(data['port'])+'/wd/hub',info)
    driver.implicitly_wait(10)
    return driver

