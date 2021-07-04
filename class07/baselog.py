'''
@author:lvming
@time:2021/6/20
'''
#再来封装日志
#组件  日志器 处理器  格式器

import logging
#创建一个日志器 别的文件使用日志  就用到这个日志器
logger=logging.getLogger()
#设置日志级别 日志信息输出info以上的级别信息
logger.setLevel(logging.INFO)

#设置日志格式  创建一个格式器  日志格式不是我们想要的
fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
formater=logging.Formatter(fmt)
#处理器  我要把日志信息输出到哪
#创建一个输出到控制台的处理器
sh=logging.StreamHandler()
#把设置的格式放到控制台去
logger.addHandler(sh)
#控制台设置格式器
sh.setFormatter(formater)

#在文件里面生成日志信息 创建处理器  文件处理器
# 处理器的作用：把日志信息输出到指定的位置
# 文件处理器创建
fh=logging.FileHandler('log1.log')#如果乱码可以写为fh=logging.FileHandler('log1.log',encoding='utf-8')
#需要把日志信息放到文件处理器里面去
logger.addHandler(fh)
#给谁设置格式，给fh设置格式
fh.setFormatter(formater)
#创建日志器 处理器：日志显示到哪些地方 控制台处理器 文件处理器 格式器  ok啦

# logging.debug('debug模式')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')