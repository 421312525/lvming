'''
@author:lvming
@time:2021/6/19
'''
# 数据库作业

# 一、为管理岗位业务培训信息，建立3个表
# S (SNO,SNAME,SDD,SAGE)
# SNO,SNAME,SDD,SAGE  分别代表学号、学员姓名、所属单位、学员年龄
#
# C(CNO,CNAME )
# CNO,CNAME        分别代表课程编号、课程名称
#
# SC(SNO,CNO,SCORE )
# SNO,CNO,SCORE      分别代表学号、所选修的课程编号、学习成绩
#
# 1.使用嵌套语句查询选修课程名称为‘税收基础’的学员学号和姓名
# (1).查的内容：学员学号和姓名 s表
# (2).条件:选修课程名称为’税收基础’
# select sno,sname from s where;
# —条件：
# Select * from c where cname=‘税收基础’；
# —一个s表一个c表，怎么把sql合在一起 分析表结构

# (select CNO from c where cname='税收基础')
# select sno from sc where cno=(select CNO from c where cname='税收基础');
# select sname,sno from s where sno in (select sno from sc where cno=(select CNO from c where cname='税收基础'));

# 2.使用嵌套语句查询选修课程编号为‘C2’的学员姓名和所属单位
#（1）拿到学号
# select sno from sc where cno='c2';
# (2)查出结果
# select sname,sdd from s where sno in(select sno from sc where cno='c2');
# (3) 联表查询方式：用到两个表  s表  学员信息 学院姓名和所属单位  sc表 课程编号为c2
# —查询所有学院的信息 条件 查哪些学员学了c2
# Select * from s,sc where s.sno=sc.sno and cno=‘c2’;

# 3.使用嵌套语句查询不选修课程编号为‘C5’的学员姓名和所属单位
# （1）找出不选修课程编号为‘C5’的学员编号
# select sno from sc where cno='c5';
# select sname,sdd from s where sno not in (select sno from sc where cno='c5');

# 4.使用嵌套语句查询选修全部课程的学员姓名和所属单位
# group by s.sno
# 分组，分组的意义 是为了统计每个学员学了多少课程
# SELECT *,count(sc.CNO) from s,sc where s.SNO=sc.SNO GROUP BY s.sno HAVING count(sc.CNO)=(SELECT count(cno) from c);
# SELECT *,count(sc.CNO) from s,sc where s.SNO=sc.SNO GROUP BY s.sno HAVING count(sc.CNO)=(SELECT count(cno) from c);
#(1)课程总数
# select count(*) from c;
# 5.查询选修了课程的学员人数
# 统计 分组
# select cno,count(cno) from sc group by cno;
# 6.查询选修课程超过5门的学员学号和所属单位
# SELECT sno,count(sc.CNO) from s,sc where s.SNO=sc.SNO GROUP BY s.sno HAVING count(sc.CNO)>5;

# 二、设计题
# 已知关系模式
# STU (SNO,SNAME)
# 学生关系。SNO 为学号，SNAME 为姓名
# CUR (CNO,CNAME,CTEACHER)
# 课程关系。CNO 为课程号，CNAME 为课程名CTEACHER 为任课教师
# STCU(SNO,CNO,SCGRADE)
# 选课关系。SCGRADE 为成绩

# 1.找出没有选修过“翠花”老师讲授课程的所有学生姓名
# select cno from c where cteacher='翠花';
# select sno from sc where cno in (select cno from c where cteacher='翠花');
# select * from s where sno not in (select sno from sc where cno in (select cno from c where cteacher='翠花'));

# 2. 列出有二门以上（含两门）不及格课程的学生姓名及其平均成绩
#查到了所有学生成绩 select * from s inner join sc on s.sno=sc.sno;
# select * from s inner join sc on s.sno=sc.sno where s.sno in (select sc.sno from sc where score<60 group by sc.sno having count(sno)>=2);
# 再查不及格  二门以上不及格
# select sno,count(sno) from sc where score<60 group by sno;

# 自己写的 select * from s inner join sc on s.sno=sc.sno where s.sno=(select sno from sc where score<60 group by sno having count(sno)>=2) and score<60;

# 3. 列出既学过“1”号课程，又学过“2”号课程的所有学生姓名
# select * from sc where cno in ('c1','c2');
# select *,count(sno) from sc where cno in('c1','c2') group by sno having count(sno)>=2;

# select *,count(sno) from sc where score<60 group by sno having count(sno)>=2;
# select sno from sc where score<60 group by sno having count(sno)>=2;
# select * from s where sno in(select sno from sc where score<60 group by sno having count(sno)>=2);

# 4. 列出“1”号课成绩比“2”号同学该门课成绩高的所有学生的学号
# select * from sc where cno='c1';
# select * from sc where cno='c2';
# select * from (select * from sc where cno='c1') as a,(select * from sc where cno='c2')as b where a.sno=b.sno;
# select * from (select * from sc where cno='c1') as a,(select * from sc where cno='c2')as b where a.sno=b.sno and a.score<b.score;
# 5. 列出“1”号课成绩比“2”号课成绩高的所有学生的学号及其“1”号课和“2”号课的成绩
