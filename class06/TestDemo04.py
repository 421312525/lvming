'''
@author:lvming
@time:2021/6/20
'''
from class06 import Demo04
from class06.Demo05 import my_db
#ctrl+鼠标点击方法  查询方法  查询员工表
# a=Demo04.insert_query('select * from emp')
# print(a)
# b=Demo04.idu_query('insert into dept(name) values("嚣张部")')


a=my_db('db.ini','TEST_DB').select_query('select * from dept')
print(a)
b=my_db('db.ini','TEST_DB').insert_query('insert into dept(name) values("可笑部")')
print(b)

