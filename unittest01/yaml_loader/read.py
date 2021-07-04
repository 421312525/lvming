'''
@author:lvming
@time:2021/6/27
'''
'''
    读取yaml中的文件内容
'''
import yaml
file = open('../Demo04_data/data5.yaml','r',encoding='utf-8')
data = yaml.load(stream=file,Loader=yaml.FullLoader)
print(data)