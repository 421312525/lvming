'''
@author:lvming
@time:2021/6/25
'''
# 数据驱动之excel读写
'''
课程回顾：
   1.基于selenium实现的关键字驱动
   2.将之前的内容基于关键字驱动的形态来实现。
      1.不必要的关键字封装
      2.在封装逻辑汇总存有一定问题。
	获取句柄
	切换到handles[0]是当前的，不需要封装
	断言的封装。
	关键字不能作为封装的函数名称。assert
	断言是要有返回结果的。
'''
'''
数据驱动：
   对于很多人而言数据驱动就是excel，yaml，ddt这样的东西。
   各种文件的数据驱动形态，只是一种实现数据驱动的形式而已。ddt是data driver test（数据驱动测试）
   数据驱动是自动化测试中提出的一个模型。原有自动化测试框架是需要将逻辑代码与测试代码进行分离。但是在自动化测试中出去代码需要管理，还有测试时使用的数据，需要进行管理。
   自动化测试代码最好是不要去改源码的前提。就需要将所有测试的过程中应用的数据内容进行单独的提取，以一个文件的形式专门提供测试数据。以便于直接修改数据文件，实现到自动化测试数据的改变。
   常规的数据驱动形式：
	1.excel
	   对于所有的测试人员都比较友好的一种形式。
	   excle形式的数据驱动可以做到一套代码多套系统的复用。对于不会python的人而言，只需要懂如何写excel文件就可以使用自动化测试。
	2.yaml
	   后续的课程会细化讲解。比较常用的一种数据驱动形式
	3.json、py
	   目前对于新首比较友好的一种模式。因为python语言相对比较熟悉的情况下，用py文件来管理数据更加容易理解和使用。
	4.其它：
	   txt、sql、xmind、xml。。。各种各样
Excel数据驱动：
   1.目前自动化测试领域主流应用的excle操作模块是Openpyxl，支持10及以上版本的excel，存有的问题就是部分函数需要手动不全，不支持自动补全。
   2.xlrd+xlwt这种是过去式了。主要用于操作03版本的excel
   Excel文件包括文件本身，sheet页，单元格。
Openpyxl来操作就需要遵循这个模式来读取所有的测试数据。

   环境搭建：
	pip install openpyxl
   直接通过import导入即可。
'''
# 反射机制

from selenium import webdriver

def open_browser(type_):
    # 基于反射的形态来简化代码
    try:
        driver = getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

# 反射机制其实就是类的表达式
# 获取属性 :在原有的类中，获取指定的属性
getattr(webdriver,'Chrome')()
# 意思就是等于webdriver.Chrome
# 如果要获取函数在括号外再加一个括号,意思就等于webdriver.Chrome()
'''
能否在函数上应用，课后试验
写法：
	setattr(attrname,value)()
	如果不能用，就是不行.应该是不可以的
'''
# 设置属性 :在原有的类中，添加新的属性或者是修改已有属性的值
setattr()
# 含有属性 :在原有的类中，判断是否存在有制定的属性
hasattr()
# 删除属性 :在原有的类中，删除已存有的属性
delattr()