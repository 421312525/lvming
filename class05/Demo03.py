'''
@author:lvming
@time:2021/6/18
'''



# 装饰器
# 装饰器：给已有的函数增加额外的功能，它的本质是一个闭包函数
# 闭包的定义：
# 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。
#闭包函数：
#形成条件：
#1.实现函数嵌套
#2.内部函数使用外部函数的变量
#3.外部函数返回内部函数，不要加括号

#写个简单的闭包
# def test1(a):
#     b=10
#     #内部函数
#     def test2():
#         #内部函数使用外部函数的变量或者参数
#         print(a,b)
#     #返回内部函数
#     return test2
# a=test1(2)
# print(a,type(a))
# a()
#print里面返回什么 2,10

#定义一个外部函数
# def outer(num1):
#     print(num1)
#     def inner(num2):
#         result=num1+num2
#         print('结果是：',result)
#     return inner
# inner=outer(3)
# inner(2)
#闭包的作用：闭包可以保存外部函数的变量，直接给内部函数去调用，不会因为外部函数调用完而销毁
#闭包函数：
#形成条件：
#1.实现函数嵌套
#2.内部函数使用外部函数的变量
#3.外部函数返回内部函数，不要加括号
#对话的过程 题目：官方提示说：不取相同名字 李四说：取相同名字
# def config_name(name):
#     #内部函数
#     def say_info(info):
#         print(name+':'+info)
#     return say_info
# tx=config_name('官方提示')
# tx('不取相同名字')
# ls=config_name('李四')
# ls('取相同名字')
#流程：config_name调用传参，返回say_info 会被tx进行接受  tx(‘不取相同名字’)==say_info(‘不取相同名字’)

#装饰器：就是给已有的函数增加额外的功能的函数
#特点：
#1.不修改已有函数的源代码
#2.不修改已有函数的调用方式
#3.给已有函数增加额外的功能

#装饰器里面的函数是函数类型，这样定义的函数才是装饰器
#发表评论的功能，先登录
#闭包的写法流程
# def check(fc):
#     print('装饰器函数执行')
#     def inner():
#         print('请先登录')
#         fc()
#     return inner
#
# def comment():
#     print('发表评论')
# a=check(comment)
# a()
#意思是想发表评论，你能不能帮我检查有没有登录  如果不想写的这么麻烦，可以用@符号，装饰器的糖写法
#@方法名
# def check(fc):
#     print('装饰器函数执行')
#     def inner():
#         print('请先登录')
#         fc()
#     return inner
# @check
# def comment():
#     print('发表评论')
# comment()
# 运行comment()，因为有check，会先去找check这个方法，check这个方法会返回inner
# 返回inner之后，comment==inner()打印  print(‘请先登录’)
# fc()==comment()这个函数，然后发表评论
# fc这个名字随意取，然后  @check check名字根据你要添加功能的名字  @check相当于check(comment)


# 类方法：类方法是针对类对象定义的一个方法
# 类方法可以直接访问类中的类属性，可以直接调用类方法
#类中的类属性 类方法
# @classmethod 在方法前定义一个classmethod，类方法里面是cls
class Tool:
    #定义类属性,用于记录创建工具对象的总数
    count=0
    def __init__(self,name):
        #实例属性，对象属性
        self.name=name
        Tool.count+=1
    @classmethod
    def show_tool_count2(cls):
        print('工具对象的总数%d' % cls.count)
    def show_tool_count(self):
        print('工具对象的总数%d'%self.count)
tool1=Tool('锄头')
tool2=Tool('斧头')
tool3=Tool('榔头')
# tool3.show_tool_count()
# tool3.count=99
# tool3.show_tool_count()
# 类里面的属性
# tool3.count=99
# tool3.show_tool_count2()
#使用类对象，直接调用类方法,不能调用实例方法
# Tool.show_tool_count2()
#作用，场景：类方法只访问类属性的时候用

#静态方法  @staticmethod
#调用类名.静态方法
#不访问实例属性，不访问类属性的时候，你就会用静态方法
# class Dog:
#     dong_dog=0
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def run():
#         print('大狗在玩耍')
# Dog.run()

# 六、设计一个游戏类
# 定义一个「类属性」top_score 记录游戏的历史最高记录
# 定义一个’实例属性’player_name 记录当前游戏的玩家姓名
# ‘静态方法’show_help显示游戏帮助信息
# ‘类方法’show_top_score显示历史最高分
# ‘实例方法’start_game开始当前玩家的游戏
# 步骤：
# 1.查看帮助信息
# 2.查看历史最高分
# 3.创建游戏对象，开始游戏
class Game:
    #记录游戏的历史最高记录
    top_score=0
    def __init__(self,player_name):
        self.player_name=player_name
        Game.top_score=99
    @staticmethod
    def show_helf():
        print('游戏帮助信息')
    @classmethod
    def show_top_score(cls):
        print('历史最高分是%d'%cls.top_score)
    def start_game(self):
        print('开始当前游戏%s'%self.player_name)
Game.show_helf()
Game.show_top_score()
xiaoming=Game('xiaoming')
xiaoming.start_game()
Game.show_top_score()



