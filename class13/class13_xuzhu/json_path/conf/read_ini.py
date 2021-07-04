'''
@author:lvming
@time:2021/7/2
'''
# 读取ini配置文件的模块
import configparser

def read_ini(path,seletion,option):
    # 读取配置文件中的内容
    conf = configparser.ConfigParser()
    # conf.read('../conf/conf.ini')
    conf.read(path)
    # url = conf.get('TEST_SERVER','url')
    value = conf.get(seletion,option)
    return value
