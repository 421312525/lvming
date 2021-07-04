'''
@author:lvming
@time:2021/6/17
'''
#异常和时间日期模块

#异常：程序在运行时如果报错了，停止，错误信息，异常
#程序停止并且提示错误信息，这个过程就叫抛出异常

#异常：为了程序的稳定性和健壮性 异常处理 就是针对突发情况做集中的处理
#语法结构


'''
try:
	尝试的代码
except:
	出现错误的处理
except BaseException as 变量名：
    出现错误的处理
程序中不确定会不会出现问题的代码，就写在try：
如果程序出现问题，就执行except里面的代码
格式：要缩进  tab
'''
#题目:要求用户输入整数
#用户输入 input string字符串 转型 int
# try:
#     # 我不确定这个代码会不会有问题
#     num=int(input('请输入数字:'))
#     print(num)
# except:
#     print('请输入正确的数字')
#针对错误类型进行处理,做出不同的响应
#2.用户输入一个数字进行2整除 except 类型
#类型：错误的最后一行前面的单词 ZeroDivisionError
#用户输入
# try:
#     num=int(input('请输入数字：'))
#     result=2/num
#     print(result)
# except ZeroDivisionError:
#     print('不能除0')
# except ValueError:
#     print('请输入正确的数字~')

#类型：
#indexError 下标索引出现问题
#keyError 字典里面的键有问题
#TypeError 对象的类型有问题
#IOError 文件打开或者关闭  流错误有问题

#未知的异常也要就行处理 BaseException 异常的祖宗 Exception
#在项目中主要用 Exception
# try:
#     num=int(input('请输入数字：'))
#     result=2/num
#     print(result)
# except ZeroDivisionError:
#     print('不能除0')
# except Exception as e:
#     print('未知的错误打印%s'%e)

#异常可以进行传递
# def demo1():
#     a=int(input('请输入数字'))
#     return a
# try:
#     result=demo1()
#     print(result)
# except Exception as e:
#     print('未知的错误打印%s'%e)

# def demo2():
#     try:
#         a=int(input('请输入数字'))
#         return a
#     except Exception as e:
#         print('未知的错误打印%s'%e)
# result=demo2()
# print(result)

# #try except作用就是用来捕获错误信息，捕获到错误的信息，会保存在日志中
# def demo03():
#     try:
#         a=int(input('请输入数字：'))
#         return a
#         demo02()
#     except Exception as e:
#         print('未知的错误打印%s'%e)
#
# result=demo03()

#完整的语法结构 用的不多
'''
try:
	尝试的代码
except:
	出现错误的处理
except BaseException as 变量名：
    出现错误的处理
else:
    没有异常的代码会执行
finally:
	无论程序有没有问题都会被执行
'''
#如果我输入2  1234
# try:
#     a=int(input('请输入整数：'))
#     result=2/a
#     print(result)
# except ZeroDivisionError:
#     print('不能除0')
# except Exception as e:
#     print('未知的错误打印%s'%e)
# else:
#     print('没有异常的代码会执行')
# finally:
#     print('无论程序有没有问题都会被执行')

#语法结构 raise异常  主动抛异常  用于特定的需求
#需求：定义一个函数,函数提示输入用户密码
# 如果用户输入的密码长度<8，抛出异常
#如果用户输入长度>=8,返回输入的密码
# def input_pwd():
#     #用户输入密码
#     pwd=input('请输入密码')
#     if len(pwd)>=8:
#         return pwd
#     exx=Exception('密码长度不够')
#     raise exx
# try:
#     u_pwd=input_pwd()
#     print(u_pwd)
# except Exception as e:
#     print('未知的异常捕获%s'%e)

# 时间 用户日志，测试报告，订单生成
# 时间：名词：时间戳  描述：从某个时间点-另外一个时间相隔的描述
# 某个时间：1970年01月01日0时0分0秒  unix操作系统 格林威治时间
import time
# 获取时间戳
# 当前时间戳 1.time 导包
# print('当前时间戳：',time.time())

# 做日期运算
# 时间元组:用9个数字表示起来的，放在元组中 年月日时分秒 一周的第几天，一年的第几天，夏令时
# t=(2021,4,1,21,25,30,3,234,0)
# print(t)
#用代码表示 tm_year tm_mon localtime())
# print('当前时间元组:',time.localtime())
# print('当前时间元组:',time.localtime(1623909133.05757))
# print('当前时间元组:',time.localtime(time.time()))

# 元组转换为时间 time.asctime()
# print('以英文的方式转为时间',time.asctime(time.localtime(time.time())))

# 时间改为系统时间  用的比较多
print('当前系统时间',time.strftime('%Y-%m-%d %H:%M:%S'))

#元组转为时间戳
# #元祖转为时间戳 time.mktime()
#制定时间转为时间戳 2021 3 12
# print('指定时间转为时间戳:',time.mktime((2021,3,12,0,0,0,0,0,0)))
#当前时间
# print('指定时间转为时间戳:',time.mktime(time.localtime()))

#时间戳转为元组 time.time()时间戳  time.localtime()元组
# print('现在的时间戳转为元组',time.localtime(time.time()))

#用的多点的  指定日期转为时间格式  2021-3-21 4:23:21  datetime和time转换指定的  项目的时候 时间
#场景
import datetime
# time_str='2021-3-21 4:23:21'
# print(datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S'))

#日历  Calendar模块 日历年历月历
import calendar
# mon=calendar.month(2021,6)
# print(mon)

#年历
# cal=calendar.calendar(2021)
# print(cal)

#局部变量还有全局变量
#局部变量：定义在方法中
#全局变量：定义在方法外  公共的，都可以使用
num = 20
def demo1():
    # 方法中如果有局部变量就拿局部变量
    # 在python中，是不允许直接修改全局变量
    # 变量的生命周期，从函数执行开始  变量创建，函数执行完了，声明周期没了，变量就屎了
    # 希望局部变量能修改全局变量，用关键字global
    # global num
    num=10
    print('在demo1函数内部的变量%d'%num)

def demo2():
    print('在demo2函数内部的变量%d'%num)
demo1()
demo2()