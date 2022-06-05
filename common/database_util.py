#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql

from config.ini_util import iniutil

"""
连接数据库,可增删改查数据操作
"""
class databaseutil():

    #host地址, user用户名, password密码,database数据库名, port端口
    iniutil().read_confini()
    host = iniutil().conf.get('mysql-test','host')
    user = iniutil().conf.get('mysql-test','user')
    password = iniutil().conf.get('mysql-test','password')
    database = iniutil().conf.get('mysql-test','database')
    port = iniutil().conf.getint('mysql-test','port')
    dbconnect=pymysql.connect(host=host,user=user,password=password,database=database,port=port)
    db=dbconnect.cursor()

    def select_all(self):
        pass

    def select_one(self):
        pass

    def update_all(self):
        pass

    def delest_all(self):
        pass


# if __name__ == '__main__':
#     connect=databaseutil().dbconnect
#     DB=databaseutil().db
#     print("数据库连接成功")
#     DB.execute("use test11;")
#     sql1 = "insert into firday values('王五');"
#     DB.execute(sql1)
#     DB.execute("insert into firday values('李k');")
#     connect.commit()
#     DB.execute('delete from firday where student="王五"')
#     DB.execute('delete from firday where student="李k"')
#     connect.commit()
#     DB.close()
#     print("数据库断开成功")
#     try:
#         sql0="select * from firday;"
#         DB.execute(sql0)
#     except:
#         print("数据库已断开连接,请连接后再试")

