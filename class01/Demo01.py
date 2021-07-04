#导入模块
#导入模块的三种方式

#1.import 模块名 调用某个模块下的内容
import class02.Demo01
class02.Demo01.tset01()
#2.from 模块 import 函数名 (这种用的多一些)
from class02.Demo01 import tset01,test02
tset01()
test02()
#3.from 模块名 import *
from class02 import *
