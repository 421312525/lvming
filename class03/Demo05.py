'''
@author:lvming
@time:2021/6/15
'''
#函数与模块
#函数：就是把具有独立功能的代码块，组织成一个小的模块
#函数：两个步骤：
#1.定义函数—封装成一个独立的功能
#2.调用函—享受 封装 的成功
# def a():
#     i=1
#     #1<5 2<5
#     while i<=5:
#         print('hello world')
#         i+=1
# a()
#函数的作用：可以提高编码的效率—重用
#函数的格式
'''
def 函数名（）：
	封装的代码
'''
#注意：def 关键字必须要填，函数名，随意命名，见名知意，不能以数字开头，不能与关键字冲突

#第一个函数的演练
# def say_hello():
#     print('hello 1')
#     print('hello 2')
#     print('hello 3')
# say_hello()
#只有调用函数的时候，函数才会被执行

#练习题目：实现两个数字求和的功能
# def sum1():
#     num1=10
#     num2=20
#     result=num1+num2
#     print('%d+%d=%d'%(num1,num2,result))
# sum1()
# 思考：只能处理固定数值。可不可以用的时候再传过来，函数传参
# def sum1(num1,num2):
#     result=num1+num2
#     print('%f+%f=%d'%(num1,num2,result))
# sum1(int(input()),int(input()))
#参数的作用：针对不同的数据进行相同的逻辑处理
#扩充：术语：函数里面的参数叫形参，在方法调用里面就叫实参
#完整的函数，实际上会有返回值 return
#在开发的过程中，有时候我们会需要一个函数运行的最终结果，这个结果就可以通过return返回过来
# def sum2(num1,num2):
#     return num1+num2
# #sum2(1,2)  值3  把3赋值给result
# result=sum2(float(input()),float(input()))
# print(result)

#空函数，是一个完整的函数  没有实际的意义，预留一个位置
# def emtpy():
# 	pass
#函数的参数：必须参数，关键字参数，默认的参数，不定长参数
#必须参数:必须以正确的顺序传入参数，调用的时候必须和申明的一致
#定义一个人的参数
# def person(name,age):
#     return '我是{}，今年{}岁'.format(name,age)
# person1=person('xiaoming',18)
# print(person1)

#关键字参数，可以通过关键字传参，不用按照顺序去写
# def person(name,age):
#     return '我是{}，今年{}岁'.format(name,age)
# person2=person(name='xiaoying',age=18)
# print(person2)

#默认参数：在定义的过程中设置默认值
# def person(name='虚竹',age=108):
#     return '我是{}，今年{}岁'.format(name,age)
#直接调用函数，可以不用参数
# person3=person()
# print(person3)
#如果说有默认值，会把原来的值覆盖掉
# person4=person(name='剑来')
# print(person4)
#如果位置参数会和关键字参数同在，先写位置参数，再写默认参数  点进方法
# def person(name,age=108):
#     return '我是{}，今年{}岁'.format(name,age)
# a=person('小a',age=109)
# print(a)
#不定长参数
#在定义的过程中不知道有多少个参数，设置成不定长度的参数,不确定多少个参数
#不定长度的参数有两种写法，* 另外一个**
#在参数前面带一个*  把参数放在元组里面
# def person(name,*args):
#     print(name,end='')
#     print(args)
# person('珠子',102,'妖','漂亮')

# *单独出现，在调用的时候通过关键字调用
# def a(num1,num2,*,num4):
#     return num1+num2+num4
# sum=a(6,7,num4=7)
# print(sum)

# def person(*args):
#     print(args)
# person(9,10,'小明','消费') #元组

#**不定长度，可以传多个参数,参数是字典的形式
# def a3(**kwargs):
#     print(kwargs)
# a3(name='张三',age=19)

# *和**同时存在
# def a4(*args,**kwargs):
#     print(*args) #加*会报错， 把数据进行解包,会按照一定的格式去解析数据
# # 在函数的参数中*args把数据转成元组的形式，**kwargs要传一个字典的格式
# # *是解析元组，**是解析字典
#     print(**kwargs)
# a4(1,2,'qiushui',name='sunny0503',age=18)
# a1=(1,2,3,)
# a2={'name':'qiushui','age':'18'}
# a4(a1,a2)

#函数嵌套 函数中再嵌套函数
#两个函数 test1(),test2()
# def test1():
# 	print('*'*50)
# 	print('test1')
#
# def test2():
# 	print('-'*50)
# 	print('test2')
# 	test1()
# 	print('+'*50)
# test2()

#匿名函数
#lambda 表达式
#语法：lambda 参数，参数：表达式
#匿名函数和普通函数
#求和
# def sum2(num1,num2):
# 	return num1+num2
# sum2(123,231)
# sum=lambda a,b:a+b
# print(sum(1,2))

#模块 py文件也就是python文件，我想要用另外一个模块中的方法
#先拿到模块，再拿里面的方法

#留的知识点：*和**  2.递归