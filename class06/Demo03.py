'''
@author:lvming
@time:2021/6/20
'''
# python连接数据库
# 需要安装数据库 的模块 pip install pymysql
import pymysql

# 用python 代码操作数据库
# 1.连接数据库
# 2.操作数据库 游标 curson 创建
# 3.关闭数据库
# show global variables like ‘port‘;mysql端口号3306
#连接数据库
# con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
# print(con)
# #创建游标
# cur=con.cursor()
# 创建部门表
# sql='create table dept(id int primary key auto_increment,name varchar(20))'
#创建员工信息表
# sql="create table emp(id int primary key auto_increment,name varchar(10),gender char(1),salary double,join_date date,dept_id int,foreign key (dept_id) references dept(id))"
#查看表结构
#describe 表名
#mysql怎么修改表结构
#1.添加字段
#alter table table_name add column column_name varchar(64);
#2.修改字段 类型
# alter table 表名 modify column 字段名 类型;
#插入部门信息数据
#sql="insert into dept (name) values ('开发部'),('市场部'),('财务部')"
#插入销售部
# sql="insert into dept(id,name) values(8,'销售部')"
#插入测试部
# sql="insert into dept(id,name) values(9,'测试部')"
# sql="insert into dept(name) values('测试部2')"
#插入员工信息
# sql="insert into emp(name,gender,salary,join_date,dept_id) values('孙悟空','男',7200,'2013-02-24',1),('猪八戒','男',3600,'2010-12-02',2),('唐僧','男',9000,'2008-08-08',2),('白骨精','女',5000,'2015-10-07',3),('蜘蛛精','女',4500,'2011-03-14',1)"
# sql='update dept set name="测试部3" where id=10'
#删除数据
# sql3='delete from dept where id=10'
# cur.execute(sql3)
# 增删改执行sql要commit，查不用
# cur.execute('commit')
# con.close()

#查询
# #连接数据库
# con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
# #创建游标
# cur=con.cursor()
# sql='select * from dept'
# #执行sql
# cur.execute(sql)
# #结果需要显示出来 fetchone()只会拿出一条数据  fetchall()拿出全部数据  fetchmany(条数)指定拿出的是几条数据
# result=cur.fetchall()
# print(result)
# con.close()

#批量增加数据
#连接数据库
con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
#创建游标
cur=con.cursor()
#执行sql
sql='insert into dept(name) values(%s)'
values=([('研发部2'),('研发部3')])
cur.executemany(sql,values)
cur.execute('commit')
#关闭数据库
con.close()

# 想在别的文件使用 应该怎么办