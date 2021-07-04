'''
@author:lvming
@time:2021/6/16
'''
#9.判断某一个字典中是否存在指定的值，如果存在，提示并且退出循环
#如果不存在，在循环整体结束后，得到一个统一的提示
#students=[{‘name’:’二狗’,’age’:’20’,’height’:1.7,’weight’:75},
#		{‘name’:’狗蛋’,’age’:’20’,’height’:1.7,’weight’:75}]

# python实现石头剪刀布的游戏
# 1.从控制台输入要输出的拳—石头(1)剪刀2、布3
# 2.电脑随机出拳—假定电脑只会出石头
# 3.比较胜负
# from random import randint
#
# player=int(input('从控制台输入要输出的拳—石头(1)剪刀2、布3:'))
# computer=randint(1,3)
# print('玩家出的是%d,电脑出的是%d'%(player,computer))
# #比较胜负 玩家的角度：赢  平局  输
# #玩家石头—电脑出剪刀
# #玩家剪刀—电脑出布
# #玩家布—电脑出石头
#
# #平局 电脑出的==玩家出的
# if (player==1 and computer==2)or(player==2 and computer==3)or(player==3 and computer==1):
#     print('玩家赢了！')
# elif player==computer:
#     print('平局')
# else:
#     print('电脑赢了')

# 递归 1到3累加
# 文件处理和os模块
# 为什么要学文件处理：操作，打开，关闭，读取文件，写入数据
#文件的作用：就是存储数据，方便下一次从文件中直接读取

#体验一下文件的基本操作：
#1.打开文件 open(文件路径，访问模式)
# 主模式:r 只读，w 只写，a 只写
# r+:在r的基础上增加可写的功能 w+：在w的基础上增加了可读的功能 a+:在写的功能上增加了可读的功能
# #rb,wb用于二进制文件
#2.写入文件

#3.关闭文件 占用服务器资源
# f=open('txtad.txt','w')
# f.write('''
# @author:lvming
# @time:2021/6/16
# @weather:sunny
# ''')
# f.close()

#r,如果文件不存在，会报错,只读
# f=open('txtad.txt','r')
# print(f.read())
# f.close()

# w表示只写，如果文件不存在，新建文件，会覆盖原有的内容
# f=open('test1.txt','w')
# f.write('aaa')
# f.close()

# a表示只写,如果文件不存在，新建文件,不会覆盖，会在后面追加新的内容
# f=open('test2.txt','a')
# f.write('\naaa')
# f.close()

# r+ 没有提前创建文件一样会报错，写入内容，会覆盖之前的内容，r+的文件指针在开头,可读可写
# f=open('test2.txt','r+')
# # 文件指针在哪 tell 光标
# print(f.tell())
# # print(f.read())
# f.write('aa')
# # print(f.read())
# f.close()

# w+:没有创建文件会新建，可读又可写,每次把之前的内容覆盖掉,文件指针,写完之后指针在尾部
# f=open('test3.txt','w+')
# f.write('qiushui')
# print(f.tell())
# #现在读取能读到数据吗？非要读取 seek偏移  seek(偏移量，指针位置)0从头开始读，1：当前位置，2结尾
# f.seek(0)
# print(f.read())
# f.close()

# a+:新建文件，指针位置，a+在最后加内容，可读和可写
# f=open('test4.txt','a+')
# f.write('sandishui')
# print(f.tell())
# print(f.read())
# f.close()

#路径：扩展一下
#1.目录下的同文件 ./当前目录
# f=open('test4.txt','r+')
# print(f.read())
# f.close()

#2.文件目录下的文件，访问外层文件目录下的文件,跨目录访问 ../
#相对路径，   绝对路径：详细地址D:\vip\vvip
# f=open('../class03/test1.txt','r')
# print(f.read())
# f.close()

#3.统计目录./ 目录名/文件名

# 读取文件 read()  readline() readlines()
# f=open('test1.txt','r')
# # print(f.read())
# print(f.read(5))
# f.close()

#只读取一行数据
# f=open('test1.txt','r')
# print(f.readline())
# f.close()

#readlines  读取到所有的数据
# f=open('test1.txt','r')
# print(f.readlines())


#指定读取
# print(f.readlines()[1])
# f.close()

# print(f.readlines()) 配套for循环
# f=open('test1.txt','r')
# for i in f.readlines():
#     print(i,end='')
# f.close()

#with..open()as  可以不用关闭文件


'''
with open(路径，模式)as 变量:
    文件操作
'''
# with open('test1.txt','r')as f:
#     print(f.read())

# f=open('test1.txt','w')
# f.write('qiushui')
# f.close()

#os模块：处理文件或文件目录的
#1.直接导入
import os
import shutil
#路径转义:用r或者\\
# file1='/Users/v_lvming/PycharmProjects/ClassStudy/class03/aa'
#创建一个文件目录
# os.mkdir(file1)

#删除文件  目录下有文件下无法删除
# os.rmdir(file1)

#删除非空文件
# shutil.rmtree(file1)

#重命名
# os.rename('/Users/v_lvming/PycharmProjects/ClassStudy/class03/aa','/Users/v_lvming/PycharmProjects/ClassStudy/class03/bb')

#获得当前文件路径 os.getcwd
# print(os.getcwd())
#当前文件的路径 os.path.join()
# path1=os.getcwd()
# print(path1)
# demo7='Demo07.py'
# print(os.path.join(path1,demo7))

#获取文件权限 os.access(path,mode)
#F_OK(是否存在),R_OK(可读) w_ok(可写) X_OK(可执行)

# file2='/Users/v_lvming/PycharmProjects/ClassStudy/class03/test4.txt'
# print(os.access(file2,os.F_OK))
# print(os.access(file2,os.R_OK))
# print(os.access(file2,os.W_OK))
# print(os.access(file2,os.X_OK))

#os.chmod

#正则
#用来处理字符串
#特点：灵活性特别强

#匹配规则： \d 匹配数字  \D
#\w字母，数字，下划线，中文
#.匹配任意字符，除\n以外
#{}前面的元素出现的次数
#？非贪婪模式 匹配1个或者0个表达式
#+匹配1个或者多个表达式
#*匹配0个或者多个表达式

#常用的方案：match()只匹配开头  search()只匹配一次  findall()
import re
# str1='.123.,.,.wowo?开始456'
#想要把数字匹配出来 导入re,没匹配出来就是none,匹配出来是个对象
# a=re.match('\d+',str1)
# a=re.match('\d+',str1).group()
# print(a)
# a=re.search('\d+',str1)
# a=re.search('\d+',str1).group()
# print(a)
# a=re.findall('\d+',str1)
# print(a)

#我想要匹配数字字母都想匹配？不匹配
# a= re.findall('\w+', str1)
# print(a)

#12、字符串”Hey, you - what are you doing here!?” 分割成 ‘Hey’,’you’,’what’,’are’,’you’,’doing’,’here’
# str2='Hey, you - what are you doing here!?'
# b=re.findall('\w+',str2)
# print(b)


#贪婪模式
# re1=re.search('e.*a','abcde123a123a')
# print(re1)
#非贪婪模式
# re1=re.search('e.*?a','abcde123a123a')
# print(re1)

# img2="<img src='test.jpg' width='20px' height='30px'>"
# re1=re.search('src=.*? ',img2).group()
# print(re1)

#递归：函数内部自己调用自己 递归：顾名思义，有去无回
#递归需要有个出口，没有出口会造成死循环
# def sum_number(num):
#当某个条件满足时，不再执行这个函数
#     if num==1:
#         return 1
#     sum_number(num-1)
# sum_number(3)

#递归算法：1+2+3
# def sum_number(num):
#     if num==1:
#         return 1
#     temp=sum_number(num-1)
#     return temp+num
# print(sum_number(3))

