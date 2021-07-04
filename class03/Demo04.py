'''
@author:lvming
@time:2021/6/15
'''
#条件判断和循环语句
#回顾一下运算符
#逻辑运算符 and or not
#比较运算符 == != >= <= > <  用于if判断
#算术运算符 + - * / %    数字操作
#赋值运算符 = += -= *= /=    数字操作
# print(1>1)
# print(1+1)
# a=3
# b=5
# a+=b
# print(a)

#逻辑运算符 and or not 两个表达式进行判断
#1.and:两个表达式都为真的时候,结果才为真,否则为假 false
#2.or: 两个表达式只要一个条件为真，就为真
#3.not:a表达式 a为真的时候，输出的就是假，全部为假的时候就是为真
# print(40>60 and 60>40)
# print(40>60 or 60>40)
# print(not 70<60)

#2.成员运算符: in  not in 在字符中找值，in在…里面’qiushui’  q if判断
#3.身份运算符: is not is 对于标识符是不是同一个对象 id()内存地址  if判断

#is和== 面试题：is 内存地址判断，==是用于字符串的判断

#学习if判断
#生活中：如果小明考试100分，妈妈就奖励一个红包，否则，妈妈就打你屁屁
#if判断：如果条件满足的话，就做这件事情，否则，就做另外一件事情，或者说什么都不做
'''
if 条件：
	条件满足的事情
else：
	条件不满足的事情
'''
#第一个if判断
#如果年龄达到18岁，就允许你进入网吧，否则，回家睡觉 运算符 比较运算符
#17>18
# age=19
# if age>=18:
#     print('允许你进入网吧')
# else:
#     print('回家学习')
# 对这个判断进行升级，想在控制台输出年龄，input在控制台输出	字符串类型不能和数字比较
# age=int(input('请输入年龄:'))
# if age>=18:
#     print('允许你进入网吧')
# else:
#     print('回家学习')
#字符串。’yuchen’判断字符串中有没有y字  运算符  in
# str1 ='yuchen'
# if 'y' in str1:
#     print('真棒')
# else:
#     print('不行')
#判断是不是同一个内存地址
# a='yuchen'
# a='qkqk'
# if id(a) is id(a):
#     print('是同一个人')
# else:
#     print('搞错了，再来')

#多重if:多个条件判断.如果你的名字是二狗子，就打虚竹一顿。如果你的名字是翠花，就嫁给虚竹,如果...
'''
if 条件1：
    执行的事情
elif 条件2:
    执行的事情
elif 条件3：
    执行的事情
...
else:
    执行的事情
'''
# 判断成绩 如果你是100分，你就是优秀的，
# # 如果你是80分，你是厉害的，如果你是70分，你是中等的， 如果你是60分，同志还需努力，否则，回家跪榴莲
# grade=int(input('请输入成绩：'))
# if grade>=100:
#     print('你是优秀的')
# elif grade>=80 and grade<100:
#     print('你是厉害的')
# elif grade>=70 and grade<80:
#     print('你是中等的')
# elif grade>=60 and grade<70:
#     print('同志还需努力')
# else:
#     print('回家跪榴莲')

# if嵌套:在条件满足的时候再加条件。
#格式:
'''
if 条件：
    要执行的事情
    if条件：
        要执行的事情
    else:
        语句
else:
    要执行的事情
'''
# grade=int(input('请输入成绩：'))
# if grade>=60:
#     if grade >= 90:
#         print('你是优秀的')
#     elif grade >= 80 and grade < 90:
#         print('你是厉害的')
#     elif grade >= 70 and grade < 80:
#         print('你是中等的')
#     else :
#         print('你及格了')
# else:
#     print('不及格，回家跪榴莲')

#循环:特定的一些事情重复执行
#两种格式：while for  在python中没有do while
'''
while格式：
while 条件:
    循环的内容
'''
# 第一个简单的while循环
# i=1
# #1<5 2<5 3<5 4<5 5=5
# while i<=5:
#     print('hello world')
#     i+=1

#题目：0+1+2+3+4+5+...+100=
#我写的
# i=0
# sum=0
# while i<100:
#     i+=1
#     sum += i
# print('i等于：'+str(i),'和为：'+str(sum))
#秋水写的
#题目：0+1+2+3+4+5+...+100=
#定义的变量，记录循环次数 100的数字都打印出来
#计算
# i=0
# sum=0
# while i<=100:
# 	print(i)
# 	sum=sum+i
# #计算器
# 	i+=1
# 	print(sum)

#在循环中有break和continue
#break当某一个条件满足时，退出循环，不执行后面的代码
#continue 当某一个条件满足时，退出循环，执行后面的代码
#打印1-10的数字，加个条件 循环到3，就退出循环
#注意：从1开始，程序里都是从0开始
# i=0
# while i<10:
#     if i==3:
#         break
#     i+=1
#     print(i)
#打印1-10的数字，加个条件 循环到3，就退出循环,continue要加逻辑
# i=0
# while i<10:
#     if i==3:
#         i = i+1
#         continue
#     i+=1
#     print(i)
#嵌套循环  循环中加循环 while for
# 题目:
'''
*
**
***
****
*****
'''
#思路：5行 5次
# row=1
# while row<=5:
#     cols=1
#     while cols<row:
#         print('*',end='')
#         cols+=1
#     print('*')
#     row+=1

#while后面加else,如果循环中止了,就不会打印else
# row=1
# while row<=5:
#     cols=1
#     while cols<row:
#         print('*',end='')
#         cols+=1
#     print('*')
#     row+=1
# else:
#     print('执行完了while循环后执行')

#for循环
#集合：元组，列表,字典    range(开始值,结束值) 左闭右开 开始值<=m<结束值
# set1={1,9.8,'lvming',(1,2,4,'yingying')}
# for i in set1:
#     print(i,end=' ')
'''
格式：
for 变量名 in 集合：
    循环体
'''
#循环5次 hello python
# for i in range(5):
#     print('hello python')

# list1=['xiaoming','xiaomi','华为',9]
# for i in list1:
#     print(i)

# 题目：0-100的累加
# sum=0
# for x in range(0,101):
#     sum+=x
#     print('sum的值%d'%sum)
# print(sum)
#循环嵌套 for 0,1,2,3,4  for循环嵌套for循环 外层for循环叫1次跑5圈，内循环就要5次
'''
*
**
***
****
*****
'''
# for x in range(0,5):
#     for y in range(0,x):
#         print('*',end='')
#     print('*')
#while循环不知道次数，for循环知道次数
