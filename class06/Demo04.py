'''
@author:lvming
@time:2021/6/20
'''
#查询
#连接数据库
import pymysql
def insert_query(query):
    con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
    #创建游标
    cur=con.cursor()
    sql='select * from dept'
    #执行sql
    cur.execute(query)
    #结果需要显示出来 fetchone()只会拿出一条数据  fetchall()拿出全部数据  fetchmany(条数)指定拿出的是几条数据
    result=cur.fetchall()
    # print(result)
    return result
def idu_query(query):
    con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
    #创建游标
    cur=con.cursor()
    #执行sql
    cur.execute(query)
    cur.execute('commit')
    return True
