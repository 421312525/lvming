'''
@author:lvming
@time:2021/6/28
'''

from time import sleep

from selenium import webdriver

'''
    python的多线程实现
    调用threading模块来实现多线程的建立,每一条线程都是独立的，彼此之间不会存在干扰
    但是在python体系下，多线程收到内存的影响，在部分情况下会出现有问题。
    当第一条线程启动的时候，初始化浏览器需要有一定的时间，于是乎在等待中，第二条线程继续运行。
    多线程不是同步运行，不是并发，只是在极短的时间内启动，每一条线程的启动都会存有时间差，只是比较短而已。
    目的是为了提升复杂测试流程的执行效率。
'''
'''
   多线程：
   所有的自动化测试在常规意义上而言都是单线程的运行模式。
   如果说是有很多的测试用例需要执行，从第一条到最后一条，一条一条依照顺序执行。
   如果有遇到比较复杂的业务场景，遇到很多需要被测试的业务场景的时候，常规的自动化测试效率将会明显下降。
   26*30分钟=780分钟，这个时候所有的自动化测试执行不再是效率，而是负担。
   所以，将没有关联性的测试用例全部进行拆分，基于并行的模式将所有的无关流程一同并行，减少测试的执行时间。
   1个流程需要30分钟，如果26个流程一同并行，所有的测试用例执行完成大约需要耗时30分钟时间。
   在selenium+python体系中，每一个浏览器的运行，都是一个后台的webdriver.exe进程，可以同步生成多个webdriver.exe进程，由不同的进程运行不同流程，从而实现，用例的并发处理。
   在python中，最直接有效的方式就是通过多线程的形态来实现。将每一个需要产生webderiver进程的内容单独作为一个线程，将所有的线程一并运行，从而实现用例的并发处理。
   
'''
import threading


def func_01():
    for i in range(5):
        print('01')
        sleep(1)
'''
   def func_01():
    for i in range(5):
        print('01')
        sleep(1) 
        
    for i in range(5):
        print('非线程:{}'.format(i))
        sleep(1)
'''
# 引入多线程的机制
# thread = threading.Thread(target=func_01)
# thread.start()
# # func_01()
# for i in range(5):
#     print('非线程:{}'.format(i))
#     sleep(1)

# 引入多线程实现自动化测试效果
def open(driver):
    driver.get('http://www.baidu.com')
    sleep(3)
    driver.quit()

# open(webdriver.Chrome())

# 定义线程组
th = []
dri1 = webdriver.Chrome()
dri2 = webdriver.Chrome()
dri3 = webdriver.Chrome()

# 引入threading模块
th.append(threading.Thread(target=open,args=[dri1]))
th.append(threading.Thread(target=open,args=[dri2]))
th.append(threading.Thread(target=open,args=[dri3]))

# 所有的线程都需要被手动调用执行
for t in th:
    # 启动线程
    t.start()
    # 等待当前线程内容执行完成再运行后续线程,就相当于变成了单线程
    '''
        如果说是多条线程对同一个文件或者对象进行操作的化。需要添加join来确保不会死锁
        也可以通过添加线程锁，让线程不会死锁。
        第一条线程运行到文件操作时，锁甲上了。其余线程就排队等待
    '''
    # t.join()