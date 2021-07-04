'''
@author:lvming
@time:2021/7/3
'''
import yaml

def load_yaml(path):
    file = open(path,'r',encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data

print(load_yaml('../data/user.yaml'))
