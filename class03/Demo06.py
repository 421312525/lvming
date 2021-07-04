'''
@author:lvming
@time:2021/6/15
'''
#上节课：*和**

#普通参数,占一个坑，传一个参数
#*是可以传多个参数，传过来的参数保存在元组中

# #**是可以传多个参数,参数，关键字传参 name='xxx'  age='xx',保存在字典中
# def demo1(*args):
#     print(args)
# demo1(1,2,3,'lvming')

# def demo2(**kwargs):
#     print(kwargs)
# demo2(name='xiaoming',age='18',sex='男')

# def demo3(*args,**kwargs):
#     print(args)
#     print(kwargs)
# a1=(1,2,3)
# a2={'name':'xiaoming','age':'18','sex':'男'}
# demo3(a1,a2)
#这里是个普通参数，args可以接收多个参数
# demo3((1,2,3),{'name':'xiaoming','age':'18','sex':'男'})
#想要把(1,2,3)传给*args，{'name':'xiaoming','age':'18','sex':'男'}传给**kwargs
# demo3(1,2,3,name='xiaoming',age='18',sex='男')
# demo3(*a1,**a2)
#一个元组
#一个元组，一个字典
#就是一个元组：元组里面有元组和字典，字典为空
#普通的传参

#作业
# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
#用什么数据结构进行学院信息的保存。学院信息：字典
#数字，字符串，元组，列表，集合，字典
# dic1=[{'name':'qiushui','age':'18','sex':'女'},{'name':'xiaoming','age':'19','sex':'男'},{'name':'yingying','age':'16','sex':'女'}]
info=[]

# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
# 系统界面如下：
# -----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
#
#界面做出来。函数

def print_info():
    print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
    print('请选择系统功能：')
    print('0:显示所有学员信息')
    print('1:添加一个学员信息')
    print('2:删除一个学员信息')
    print('3:修改一个学员信息')
    print('4:查询一个学员信息')
    print('exit:退出学生管理系统')
    print('*'*50)
# 添加的功能
# 1.用户帮你输入学员信息:输入学员的编号，学员的姓名，学员的性别
# 2.输入完信息要保存起来.保存在字典里面
#思考：需求如果有名字相同，给我个提示：学员编号已存在
#1.循环，应该把班级里面的所有的编号循环一遍
#2.判断，有没有编号相同
def add_stu():
    new_id=input('请输入学员的编号：')
    new_name=input('请输入学员的姓名：')
    new_sex=input('请输入学员的性别：')
    # 1.循环，应该把班级里面的所有的编号循环一遍 {}字典取值，键值对
    for i in info:
        print('所有学员信息%s'%i)
    # 2.判断，有没有编号相同
        if i['id']==new_id:
            print('用户已存在')
            # break退出循环 return不会执行下面代码
            return
    #创建一个空字典
    info_dict={}
    #把数据保存在字典中，字典新增
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['sex']=new_sex
    print(info_dict)
    #班级是不是info 怎么把字典放到列表中
    info.append(info_dict)
    print(info)
    #按1能实现这个功能，封装成函数。按1的时候，调用函数
    #写在while循环上面
#删除一个学员信息
#1.用户输入学员的姓名，学员存在就删除
#如果学员不存在就提示该学员不存在
#把所有的学院信息遍历出来
def del_stu():
    del_name=input('请输入要删除的学员姓名：')
    for i in info:
        if i['id']==del_name:
            info.remove(i)
            break
    #for else整个循环结束后,才做的事情
    else:
        print('该学员不存在')
    print(info)
#修改学员
#1.用户输入学员的姓名，学员存在就修改
#如果学员不存在就提示该学员不存在
#把所有的学院信息遍历出来
def upd_stu():
    upda_stu=input('请输入要修改的学员姓名：')
    for i in info:
        if i['name']==upda_stu:
            #给个新名字
            i['name']=input('请输入新名字：')
            break
    else:
        print('要修改的学员不存在')
    print(info)
#查询学员信息
def search_info():
    search_stu=input('请输入要查询的学员姓名：')
    for i in info:
        if i['name'] == search_stu:
            print(f"学员信息：编号是{i['id']},姓名是{i['name']},性别是{i['sex']}")
            break
    else:
        print('请输入要查询的学员')
    print(info)
#查询所有学员信息
def search_all():
    for i in info:
        print(f"{i['id']},{i['name']},{i['sex']}")
while True:
    print_info()
    #用户需要输入
    user_info=int(input('请输入功能序号：'))
    #判断输入的是什么序号
    if user_info==0:
        # print('0:显示所有学员信息')
        search_all()
    elif user_info==1:
        # print('1:添加一个学员信息')
        add_stu()
    elif user_info==2:
        # print('2:删除一个学员信息')
        del_stu()
    elif user_info==3:
        # print('3:修改一个学员信息')
        upd_stu()
    elif user_info==4:
        # print('4:查询一个学员信息')
        search_info()
    elif user_info==5:
        print('exit:退出学生管理系统')
        break
    else:
        print('输入有误')
#
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
#
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
#
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
#
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
#
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
#
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。











