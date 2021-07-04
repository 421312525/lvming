'''
@author:lvming
@time:2021/6/20
'''
import configparser
import pymysql

#专门用来写数据库内容的
class my_db:
    #连接 init函数 初始化函数 只要调用类，就会执行这个Init函数
    # 连接不确定会不会有问题
    def __init__(self,configPath,DB):
        try:
            config=configparser.ConfigParser()
            config.read(configPath)
            host=config[DB]['host']
            port=int(config[DB]['port'])
            user = config[DB]['user']
            passwd=config[DB]['password']
            db_name = config[DB]['database']
            # charset=config[db]['charset']
            #连接不确定会不会有问题
            self.con=pymysql.connect(host=host,port=port,user=user,password=passwd,database=db_name)
            # self.con=con=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='Yingying520',database='test01')
        except Exception as e:
            print(e)
    #创建游标
        self.cur=self.con.cursor()

    #增删改查
    def select_query(self,sql):
        try:
            #执行sql语句
            self.cur.execute(sql)
            #显示结果
            result=self.cur.fetchall()
            return result
        except Exception as e:
            print('查询失败%s'%e)

    def insert_query(self,sql):
        try:
            #执行sql语句
            self.cur.execute(sql)
            self.cur.execute('commit')
            return True
        except Exception as e:
            self.cur.execute('rollback')
            print('增删改失败%s'%e)
