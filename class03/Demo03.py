'''
@author:lvming
@time:2021/6/13
'''
#可变数据类型 字典dict 列表list  集合set

#不可变数据类型 元组tuple
#定义：（）来表示，数据是可以放任意类型的数据，数据之间用,隔开
#创建一个空元组
# tup1=()
# print(tup1,type(tup1))
#元组里面放数据
# tup2=(1,2.3,'lvming',True)
# print(tup2,type(tup2))
#在元组中要放一个数据，在数据后面加个， ()可以表示数学中(1+1)*2 python会将括号当做数学中的括号
# tup3=(1,)
# print(tup3,type(tup3))
# typ3=(1)
# print(typ3,type(typ3))
#访问lvming 下标/索引的访问 从0开始 元组里面还支持切片 tup[开始索引:结束索引:步长]  左闭右开
# tup=(1,2.3,'lvming',True)
# print(tup[2])
# 访问2.3，'lvming'
# print(tup[1:3])
# print(tup[1:-1])
# print(tup[-3:-1])
# print(tup[-2:-4:-1])

#元组进行增删改 不可以  不可变数据类型
# tup5=(1,2.3,'lvming',True)
# #拼接方式 + 增加数据
# tup6=('虚竹',)
# s=tup5+tup6
# print(s)
# print(tup5+tup6)

#删除'lvming' del  不可以只删除元组中的一个数据
# del tup5[2]
# print(tup5)
#del可以删除整个元组
# del tup5
# print(tup5)

# 复制*
# print(tup5*2)
#元组的长度 len获得长度
# print(len(tup5*2))

#可变数据类型 列表 list:是一种有序的集合，对数据进行增删改,使用最频繁的一种数据类型 数组
#定义:[]进行标识，数据任意类型，用,隔开
# list1=[]
# print(list1,type(list1))
# list2=[1,9.8,'lvming',(2,1,True)]
# print(list2,type(list2))

#访问列表中的数据  下标,支持切片
# list3=[1,9.8,'lvming',(2,1,True)]
#访问lvming
# print(list3[2])
# 访问最后2个数据 'lvming',(2,1,True)
# print(list3[2:])
# 索引越界list index out of range
# print(list3[5])

#对于列表进行增删改
#增加数据 append()往末尾加一条数据 insert()指定位置加数据 extend()在末尾增加数据
#append()和extend()在后面加多个对象，append直接插入对象，extend拆分对象插入
# list4=[1,9.8,'lvming',(2,1,True)]
# list4.append('5')
# print(list4)
# list4.insert(1,'狗蛋子')
# print(list4)
# list4.extend('翠花')
# print(list4)
# list4.append([1,2,3])
# print(list4)
# list4.extend([1,2,3])
# list4.extend([113,21231,33123])
# print(list4)

# 修改 索引进行修改，从0开始
# list5=[1,9.8,'lvming',(2,1,True)]
# #把lvming修改为dengying
# list5[2]='dengying'
# print(list5)

# 删除 pop通过索引进行删除 remove指定数据进行删除 del删除一个或者连续几个元素或者整个元素删除
# list6=[1,9.8,'lvming',(2,1,True)]
# pop通过索引删除,并且删除会返回删除的数据
# print(list6.pop(2))
# pop是可以不填参数，默认删除最后一个元素
# print(list6)
# print(list6.pop())
# print(list6)

#remove删除 通过元素删除 ()括号里面一定要填数据 remove删除不会返回删除的数据
# print(list6.remove('lvming'))
# print(list6)

#del删除一个或者连续几个元素或者整个元素删除  支持切片
# del list6[1]
# print(list6)
# del list6[1:3]
# print(list6)
# del list6
# print(list6)

# 支持切片几个元素
# del list6[1:3]
# print(list6)

#一整个元素删掉
# del list6
# print(list6)

#题目：有重复的元素怎么删除
# list7=[1,1,9.8,'lvming',9.8,(2,1,True)]
#统计一下重复的元素 count(数据)  不知道哪个是重复的数据  方式
# print(list7.count(1))
# 找到1的下标进行删除,找1  可以用find和index(找的值，开始索引,结束索引)
# 区别:find没找到会返回-1,index没找到会报错
# print(list7.find('1',0,4))
# list7.index(1,0,4)
# print(len(list7))
# print(list7.index(1,0,len(list7)))
# print(list7.index(1))
#删除 索引
# print(list7.pop(0))
# print(list7)
# print(str(list7),str(list7).find('lvming'))

#不知道哪个是重复的数据  方式max()
# list7=[1,1,9.8,'lvming',9.8,(2,1,True)]
# print(max(list7,key=list7.count))
#list运算符 + *
# list7=[1,1,9.8,'lvming',9.8,(2,1,True)]
# list6=[3,5,7]
# print(list6+list7)
# print(list6*2)

#其它操作
list6=[9,4,3,5,7]
#排序  升序 list.sort
# list6.sort()
# print(list6)
#降序
# list6.sort(reverse=True)
# print(list6)
#翻转
# list6.reverse()
# print(list6)

#数据类型转换
#元组转为列表
# tup10=(1,'er')
# print(list(tup10),type(list(tup10)))
# list8=[1,'er']
# print(tuple(list8),type(tuple(list8)))

# 字典:字典：也是用来存储数据，除了列表以外，最灵活的数据
# 定义：{key1:value,key2:value,}key1键，value值 键值对，注意：key是唯一的
# 创建一个空字典
# dict1={}
# print(dict1,type(dict1))
#字典中有数据
# dict2={'name':'lvming','age':18}
# print(dict2,type(dict2))

#访问字典中的数据  通过键的方式访问  重点：字典，列表是怎么访问数据
# print(dict2['name'],dict2['age'])

#字典进行增删改
#增加数据 sex 增加一个键值对
# dict3={'name':'lvming','age':18}
# dict3['sex']='男'
# print(dict3)
#
# #修改name
# dict3['name']='yingying'
# dict3['sex']='女'
# print(dict3)

#删除 pop(指定键删除) popitem(删除最后一个) del[指定键删除]或整个
# del dict3['name']
# print(dict3)
# del dict3
# print(dict3)
# dict3.pop('age')
# print(dict3)
# print(dict3.popitem())
# print(dict3)

#dict3中更新dict4中的数据  键不重复 键是相同的是更新数据，键是不同的增加数据 ***
# dict3={'name':'lvming','age':18}
# dict4={'name1':'dengying','sex':'女','age':'6'}
# dict3.update(dict4)
# print(dict3)

#字典转成字符串
# dict5={'name':'lvming','age':18}
# print(str(dict5),type(str(dict5)))
# # 字符串转为字典 eval() ****
# dict5="{'name':'lvming','age':18}"
# print(eval(dict5),type(eval(dict5)))

#items 一次性拿到字典中所有的键值
# dict6={'name':'lvming','age':18}
# for i,j in dict6.items():
#     print(i,j)

#创建一个新的字典  formkeys(键列表，值)
# list11=['name','age','sex']
# dict7={}
# dict8=dict7.fromkeys(list11,1,)
# print(dict8)

#集合set 是一种无序的
#定义：{}或者set进行标识，数据也是任意的
#创建一个集合
# set1={1,2,3,4,'lvming'}
# print(set1,type(set1))
# set2=set((1,2,3,4,'lvming'))
# print(set2,type(set2))

#创建一个空的
# set3=set()
# print(set3,type(set3))

#访问set中元素 不能访问，因为是无序的
# set2=set((1,2,3,4,'lvming'))

#进行增删改
# set2=set((1,2,3,4,'lvming'))
# set2.add(5)
# print(set2)
# set2.update((5,6,7,8))
# print(set2)
#删除 remove指定元素删除 pop任意元素删除 discard指定元素(没有找到元素也不会报错) clear删除所有元素
# set2.remove(2)
# set2.pop()
# set2.discard(3)
# set2.clear()
# print(set2)

#作用：对集合操作，重复去操作
# 交集&：两个集合中相同的元素
# 并集|：两个集合中所有的元素，去重
# 差集-：返回a所有的元素，a重复的元素不要
# 补集^：返回两个集合中所有的元素，重复元素不要
# set1=set((1,2,3,4,5))
# set2=set((7,8,9,5))
# print(set2&set1)
# print(set2|set1)
# print(set2-set1)
# print(set2^set1)
#
# #想不换行 ,
# a=[1,2,3,4,5,6,4]
# for i in set(a):
#     print(i,end=',')
