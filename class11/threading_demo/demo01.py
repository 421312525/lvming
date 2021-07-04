'''
@author:lvming
@time:2021/6/28
'''
from time import sleep

'''
    selenium grid模块的分布式部署
    Grid:
       Selenium Grid。是selenium家族存在时间特别有就，但是又鲜有人使用的组件。使用有难度限制
       是一个分布式部署的组件。是分布式形态中最为典型的一种，叫做MS的形态。
       M表示主节点，不干活只下发任务
       S表示从节点，只干活
       核心环境：
        1.M环境
        2.S环境
           两者环境保持一致
           1.JDK：百度安装指南
           2.Selenium Stand alone.jar：在selenium官网下载。
           3.webdriver.exe：浏览器驱动，版本对应即可
        3.部署M节点
           1.java -jar ./Selenium Stand alone.jar -role hub -port 4000
        4.部署S节点
           1.java -jar ./Selenium Stand alone.jar -role node -hub http://192.168.xx.xx:4000/grid/register -port 5000
    Remote创建grid的浏览器对象，webdriver创建selenium的浏览器对象
    这个技术在面试的时候用来装逼，以及对于现有自动化测试框架体系技术做一个效率提升。和自动化测试精进很有帮助
    课后练手：
	1.部署selenium grid
	2.结合多线程的用例并发，将原有的关键字驱动+Excel驱动实现一个excel一个线程的形态。
	3.尝试基于UnitTest来实现多线程用例并发处理。
'''

# 通过grid模块创建浏览器驱动对象
from selenium.webdriver import Remote
import threading

# 引入多线程实现自动化测试效果
def open(driver):
    driver.get('http://www.baidu.com')
    sleep(3)
    driver.quit()

# 定义所有Node节点信息:M节点是不干活的,只需要写入所有的子节点信息即可
hotsts = {'http://172.21.194.56:4000/wd/hub':'chrome',
          'http://172.21.194.56:5000/wd/hub':'chrome',
          'http://172.21.194.56:6000/wd/hub':'chrome'}

# 定义线程组
th = []
# 基于节点创建浏览器对象
for host,browser in hotsts.items():

    driver = Remote(command_executor=host,
                    desired_capabilities={
                        "platform":"Windows",# mac的是OS
                        "browserName":browser
                    })
    # 将创建好的driver对象，创建对应的线程任务。
    th.append(threading.Thread(target=open,args=[driver]))

# 启动所有的已存线程
for t in th:
    t.start()



