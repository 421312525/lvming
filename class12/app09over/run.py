'''
@author:lvming
@time:2021/6/30
'''
import HTMLTestRunner
import unittest


# discover(目录文件，执行的文件)
dict_dir = './test_case'
# 找用例文件
discover = unittest.defaultTestLoader.discover(dict_dir,'test_login.py')
with open('./reports/report1.html','wb')as f:
    HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2).run(discover)

#


