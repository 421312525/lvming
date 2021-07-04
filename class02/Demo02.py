# #数据类型
# #1.可变数据类型:字典dict  列表list  集合set
#
# #2.不可变数据类型:数字number  字符串string  元组tuple
#
# #数字number  整数:int  小数:float  bool:True 1 False 0
# a=1
# print(a)
# print(type(a))
#
# b=1.5
# print(b)
# print(type(b))
#
# c=True
# print(c)
# print(type(c))
#
# print(True==1)
# print(True==0)
# print(False==1)
# print(False==0)
#
#数字可以进行运算 + - * /除 %取余数  **乘方  //整除
# a1=19
# b1=8
# print(a1+b1)
# print(a1-b1)
# print(a1*b1)
# print(a1/b1)
# print(a1%b1)
# print(a1**b1)
# print(a1//b1)
#
# #比较运算符 == >= <= > < !=  只有True和False  =赋值
# print(1==1)
# print(1!=1)
# print(1<=1)
# print(1>=1)
# print(1<1)
# print(1>1)

#赋值运算符 = += -= *= /=
# a3=6
# b3=7
# a3+=b3
# print(a3)
# a3-=b3
# print(a3)
# a3*=b3
# print(a3)
# a3/=b3
# print(a3)

# 数据类型进行转换
# a5=1.5
# b5=1
# #浮点型
# print(a5,type(a5))
# print(int(a5))
# #整型
# print(float(b5))

#数字的常用函数
#abs()绝对值
# a6=-12
# print(abs(a6))
# a7=3
# print(abs(a7))

#向上取整ceil() 天花板   操作小数
#向下取整floor() 地板
#输入math进行导包 alt+enter  a
# import math
#
# a8=1.5
# print(math.ceil(a8))
# print(math.floor(a8))

# 保留几位小数  3.1415926 round 格式定义 round(数字，保留位数)
# print(round(3.141592657,3))

#随机数  在区间内任意输出一个数 random()默认0-1的随机数，randint(区间)0,20  0,30
import random
# #默认输出0,1
# print(random.random())
# print(round(random.random(),3))
# print(random.random())
# print(random.randint(0,29))

# 字符串 定义：单引号、双引号、三引号
# str1='小明'
# str2="明"
# str3='''小
# 明'''
# print(str1,str2,str3,type(str1),type(str2),type(str3))

# 字符串的切片  作用：由一个大的字符串切成一个小的字符
# 格式:str[开始值:结束值:步长] 开始值 从0开始 结束值是左闭右开 0-8  0,1,2,3,4,5,6,7
# 步长就是间隔，默认1
# 从左往右取，从0开始取
# 从右往左取，从-1开始取
# str4='python123'
# print(str4)
# #输出thon
# print(str4[2:6:1])
# #输出123
# print(str4[6:9])
# print(str4[6:])
# print(str4[-1:-3]) #为空
# print(str4[-3:-1]) #12  因为左闭右开
# print(str4[-3:])
# #输出最后一个字符
# print(str4[8])
# print(str4[-1])
# #步数为2
# s=str4[2:6:1]
# print(s[::2])
# print(str4[::2])
# #字符串的翻转
# print(str4[::-1])
# 字符串和数字是不可变的
# a='abc'
# print(id(a))
# a='abcd1'
# print(id(a))
# print(a)

# 字符串中的运算符 +拼接 *复制 *几次
# str8='aaaa'
# str9='123'
# print(str8.join(str9))
# print(str8+'b')
# print(str8*2)
# seq = ['a','b',1,2]
# jn = '-'
# print(jn.join(map(str,seq)))

#特殊字符 \n换行， \t制表符，可以进行缩进
# str8='abc\ndef'
# print(str8)
# str9='\tdawdawdaga'
# print(str9)
# #\反斜杠  单处\是进行换行 路径 \关键字  把地址输出两种方式： r 或者 再加个\
# str10='\\Users\\v_lvming\\PycharmProjects\ClassStudy'
# print(str10)
# str11=r'dqdwqd\nqrqrwqr\qrwqqrwq'
# print(str11)

# 字符串的格式化,格式化 把名字和年龄传进去
# 1.通过占位符进行站位 %s字符串 %d数字类型 %f浮点类型...
# print('xxxx真漂亮,今年xxx岁')
# print('%s真漂亮,今年%d岁'%('颖颖',18))
# # 2.format格式进行占位
# print('{}真漂亮,今年{}岁'.format('小明',18))
# # 还可以指定顺序执行
# print('{1}真漂亮,今年{0}岁'.format('小明',18))
# #f-string format格式的改良版
# name='小朋友'
# age=6
# print(f'{name}真漂亮，今年{age}岁')

#字符串的分割和连接 split join
#split分割 格式：split(分割内容，次数)
#split()分割空白或者\t \n进行分割
# str10='sa-da\nf-aa\tfg-ga=fag'
# print(str10.split())
# print(str10.split('-'))
# print(str10.split('-',1))
# print(str10.split('a'))
#join 连接
# str11=' '
# str12='ssssss'
# print(str11.join(str12))

#字符串的内置函数 replace替换
# str11='xiaoming123'
# print(str11.replace('123','xiao'))
# print(str11.replace(str11,'xiao'))

# #统计字符串的长度
# str12='xiaoming123'
# print(len(str12))

#查找字符串find(str,开始索引，结束索引)
#如果没有找到这个数的话，会返回一个-1   找到会返回索引
# str12='fdsfdsdsagsdf'
# print(str12.find('s'))
# print(str12.find('s',4,7))
# print(str12.find('s',11))

#判断字母或者数字
# str12='fdsfdsdsagsdf'
# #判断数字还是字母
# print(str12.isalnum())
# #判断是小写
# print(str12.islower())
# #判断是不是数字
# print(str12.isnumeric())

#常见的字符串大小写转换
# str12='fdsfdsdsagsdf dawd w a daw '
# print(str12.split(' '))
# print(str12.split('d'))
# print(str12.upper(),str12.lower(),str12.capitalize())
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('www.baidu.com')

