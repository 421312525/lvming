'''
@author:lvming
@time:2021/6/18
'''
# 数据库（一）
# 登录数据库
# /usr/local/MySQL/bin/mysql -u root -p
# 假设远程主机的IP为：23.106.134.88，用户名为root,密码为123456，打开终端，输入如下命令：mysql -h 23.106.134.88 -u root -p 123456。
# 例如：mysql -h 10.143.83.32 -u wenkudb_all_r -pwenkudb_all_r123 -P 6000 docshare --default-character-set=utf8 -A --vertical
# 数据库：存放数据的仓库
# 数据表：
# 存具体数据的地方
# 常用的数据库：
# Mysql:开源并且免费的数据库，小型 Oracle公司的
# Oracle:收费的大型数据库  银行
# Db2:IBM公司的数据库，收费的，银行
# Sql server:中型数据库，.net C#等语言使用
# 数据库：存放数据的仓库
# 数据表：
# 存具体数据的地方
# 常用的数据库：
# Mysql:开源并且免费的数据库，小型 Oracle公司的
# Oracle:收费的大型数据库  银行
# Db2:IBM公司的数据库，收费的，银行
# Sql server:中型数据库，.net C#等语言使用
#
# 最常见的Mysql：免费  功能强大
#
# 装mysql
#
# 输入mysqld —defaults-file=my.ini — initialize-insecure  命令

# 装mysql
# 图形界面工具：navicat sqlyog
# 1,操作数据库 安装mysql管理系统  图形工具
# 2.操作数据库  1.鼠标点点 2.sql语句  结构化查询语句
# sql语法；
# 1.不区分大小写
# 2.每句sql语句后面加个;

# —创建自己的数据库 —注释  备注的意思
# —语法 create database 数据库名；
# —CREATE database test55;
# —删除数据库的语法：drop database 数据库名；
# DROP database test55;
# —创建表 语法：
# /*
# —create table 表名(
# 字段名 字段类型，
# 字段名 字段类型，
# 字段名 字段类型
# Varchar 字符串 约束条件  主键外键
# Char 性别
# )
# **/
# CREATE TABLE test55.student(
# 	id int,
# 	name varchar(20),
# 	sex char(10),
# 	age int
# )；
# —表中添加数据
# — 字段全部添加：
# insert into student values(值，值，值。。);
# —insert into student values(1,’钟灵’,’女’)；
# —部分添加：insert into 表名(字段，字段，字段) values(值，值，值。。)
# insert into student(id,name,age) values(1,’小明’,16);
# —插入多条数据
# —insert into student values(3,’钟灵’,’女’,18),(4,’钟灵’,’女’,18),(5,’钟灵’,’女’,18),(6,’钟灵’,’女’,18);
#
# —查询数据
# —查询全部：select * from 表名；
# —查询部分字段：select 字段名，字段名 from 表名；
# select * from student;
# select id,name from student;

# —修改
# —Update 表名 set 字段名=值   值有时候会加’’有时候不加，根据数据类型来定
# —字段名=值 把这一列数据改成你想要的值
# Update student set age=19
# Select * form student;
# —只想改一行的某个值 update 表名 set 字段名=值 where 字段名=值
# update student set age=16 where id=4;
# select * form student;
#
# —删除 delete from 表名 where 字段名=值  where条件  满足条件则
# —删除表数据  delete from 表名
# delete from student where name=‘钟灵4’;
# Delete from student;
# Select * from student;
# truncate table stu;
# select * from;
# — drop table 表名; 可以删掉表结构
# drop table student;

# —查询别名：select 字段 as 别名，字段 as 别名 from 表名;
# select id as 编号， name 姓名 from stu;
# select st.id as 编号， st.name 姓名 from stu st;
#
# —查询 还有查询条件
# —运算符 大于>  小于< 等于= 小于等于<= 大于等于>= 不等于!= 不等于<>
#
# —加条件查询 where 条件查询
# —语法结构：select * from 表名 where 条件；
# —查询数学成绩大于80分的学生
# select * from student3 where math>80;
# —查询数学成绩大于等于98分的学生；
# select * from student3 where math>=98;
# —查询数学成绩小于等于99分的学生
# select * from student3 where math<=99;
# select * from student3 where math!=99;
# select * from student3 where math<>99;
#
# BETWEEN 100 and 200 区间  包头又包围
# 英语成绩在
# select * from student where English between 75 and 90;

# 数据库（二）
# in like
# in 在。。。里面 只要满足条件就会查询出来
# —查询student3表中的id为1 或者  id为2 或者 id为3的学院
# select * from student;
# Select * from student3 where id=1 or id=2 or id=3;
# Select * from student3 where id in(1,2,3,);
# 如果in当中的数字不存在，查询只显示存在的
# select * from student3 where id in(1,42,3);
# not in 不在…里面
# select * from student3 where id not in(1,2,3);

# — like 模糊查询  %匹配任意多个字符串  _匹配一个字符
# —查询姓马的学员
# select * from student3;
# select * from student3 where name like ‘马%’;
# —查询姓名中包含’化’字的学员
# select * from student3 where name like ‘%化%’；
# —查询姓马的学员，姓马只有2个字
# select * from student3 where name like ‘马_’;
#
# —and or 逻辑运算
# —and 和 同时满足才是真的 or 只有一个条件满足就对了
# —查询年龄大于35岁并且性别为男的学生
# Select * from student3 where age>35 and sex=‘男’；
# —查询年龄大于35岁或者性别为男的学生
# Select * from student3 where age>35 or sex=‘男’;

# —排序  按照什么字段进行排序
# — 语法 order by 字段名 desc/asc 默认asc desc降序 asc升序
# select * from student3 order by age ;
# Select * from student3 order by age asc;
# Select * from student3 order by age desc;
# select * from student3 where name like ’马%’ order by age desc;

# 问题：根据年龄进行排序，年龄相同的话根据数学成绩比较
# select * from student3 order by age asc;
# select * from student3 order by age asc,math desc;

# —聚合函数
# —一列一列的，根据一列的值返回结果
# 常用的几个函数
# —max(列名) 求这一列最大的值
# —min(列名)求这一列最小的值
# —avg(列名)求这一列的平均值
# —count(列名)统计这一列有多少数据
# —sum(列名)求这一列的总和；
#
# select * from student3;
# —查询年龄最大的学员
# Select max(age) from student3;
# —查询年龄最小的学员
# Select min(age) from student3;
# —查询数学的平均成绩
# Select avg(math) from student3;
# —统计有多少行数据
# select count(id) from student3;
# select count(*) from student3;
# select count(1) from student3;
# —求数学成绩总分数
# select sum(math )from student3;

# —分组
# —想把男和女分组
# —单独分组没什么用，分组的目的是为了统计一些数据，一般分组会和聚合函数一起使用  分在男足是为了统计男组的人数还是男组的成绩
# select * from student3 group by sex;
# —统计男女组各有多少人
# select count(*),sex from student group by sex;
# —统计男组数学平均成绩和女足的数学平均成绩
# select avg(math),sex from student3 group by sex;
#
# —查询年龄大于25岁，按性别分组，统计每组的人数。
# select count(*),sex from student3 where age>25 group by sex;
#
# —查询年龄大于25岁，按性别分组，统计每组的人数，显示性别人数大于2数据
# select count(1),sex from student3 where age>25 group by sex having count(1)>2;
#
# —where 与having都是加条件
# Where在分组之前过滤数据，where后面不可以聚合函数
# —having在分组之后过滤数据，可以用聚合函数
#
# 分页 limit 限制一页显示多少条数据
# —limit 起始数 0开始 总共显示多数 limit 3,6
# select * from student3 limit 2,5;
# Select * from student3 limit 5;

# *****
# #创建部门表
# create table dept(
# Id int primary key auto_increment.
# name varchar(20)
# );
# —表约束  primary key主键，唯一标识符，id
# —auto_increment 自增
# —foreign key外键
# —外键：foreign key(编号) re
# —多表查询
#
# Inset into dept (name) values (‘开发部’),(‘市场部’),(‘财务部’)；
#
# #创建员工表
# create table emp(
# id int primary key auto_increment,
# name varchar(10),
# gender char(1),—性别
# salary double,—工资
# join_date date,—入职日期
# depy_id int,
# foreign key (depy_id) references dept(id)
# );
# —外键，关联部门表（部门表的主键）
# )
# insert into emp(name,gendar,salary,join date,dept_id) values(‘孙悟空’,’男’,7200,’2013-02-24’,1);
#
# select * from dept;
# select * from emp;
#
# —需求：想查询出员工信息，员工的编号，姓名，性别，工资，入职日期，部门名称
# —关联隐式写法
# select emp.id,emp.name,gendar,salary,join_date,dept.name from emp,dept where emp.dept_id=dept.id;
#
# —inner join on 内连接
# select emp.id,emp.name,gendar,salary,join_date,dept.name from emp inner join dept on emp.dept_id=dept.id;
#
# —left join on 左连接 以左表为基准
# select emp.id,emp.name,gendar,salary,join_date,dept.name from emp left join dept on emp.dept_id=dept.id;
#
# —right join on 右连接 以右表为基准
# select emp.id,emp.name,gendar,salary,join_date,dept.name from emp right join dept on emp.dept_id=dept.id;
#
# 给表取别名
# select e.id,e.name,gendar,salary,join_date,d.name from emp e,dept d where e.dept_id=d.id;
#
#
# —列出至少有2个员工的所有部门
# 1.查出员工的信息
# Select * from emp e,dept d where e.dept_id=d.id;
# 2.根据部门进行分组
# Select count(*),d.name from emp e,dept d where e.dept_id=d.id group by d.name having count(*)>=2;

# 数据库（三）
# —子查询 python怎么链接sql




