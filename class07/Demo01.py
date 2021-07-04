'''
@author:lvming
@time:2021/6/20
'''
#日志：文档  文件 日志  记录系统运行的内容
#日志的作用：能够记录在系统上面进行的操作  记录系统运行状态  出现问题也能够很快定位问题

#学习日志
#几个组件
#1.loggers：日志器  提供应用程序代码直接使用的接口
#2.handlers：处理器  用于将日志记录发送到制定的目的位置
#3.formatters：格式器  用于控制日志信息的最终输出格式
#filters提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出(其它的日志记录将会被忽略)

#日志级别 info  error 能够反映出问题的严重程度
#debug：调试的级别  1级别
#info：正常的级别 2级别
#warning：警告 程序有问题但是不影响程序正常运行 3级别  不提bug 默认的级别
#error：错误  程序有问题  4级别
#critical：严重的问题 程序崩溃了 5级别

import logging
#自带的，不需要安装
#可以用别人已经封装好的
# import loguru
# loguru.logger.info('info')

#设置日志的级别 日志的格式不是我们想要的，设置格式 格式的字符串
#日志信息输出到控制台 为什么要把日志信息输出到文件里面？
# 日志事件发生的时间:%(asctime)s pathname的文件名部分:%(filename)s 日志级别：%(levelname)s
# 调用日志记录函数的函数名:%(funcName)s   日志记录的文本内容:%(message)s
# 基础配置写法，1.日志信息不能在控制台和文件里面同时出现 2.会乱码
# 函数的内容：就是设置了日志的格式，日志保存在哪
def test_log():
    fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    logging.basicConfig(level=logging.DEBUG,format=fmt,filename='log1.log')
    return logging

# logging.debug('debug模式')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')

# 日志文件，你想要放在目录下，就要自己创建目录
#1.封装成方法，配置温度计  conf ini
#格式：
# [模块]
# #模块的内容 键值对的方式
# [模块的细节]
# 细节
# loger_xx细节 设置日志级别 日志处理器
# #handlers_xx的细节 输出内容到哪
# formatters_xx的细节 日志格式