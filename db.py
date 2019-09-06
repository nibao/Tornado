#!/usr/bin/python3
import pymysql
from contextlib import contextmanager


# 非连接池模式
_CONF = {}


    # 使用 cursor() 方法创建一个游标对象 cursor

#dbconfig为数据库初始化参数，从main函数中传入配置信息获取
def init_db(dbconfig):
    #使用全局变量_CONF并赋值
    global _CONF
    _CONF = dbconfig

@contextmanager
def get_cursor():
    conn = pymysql.connect(host=_CONF['host'],user=_CONF['user'],passwd=_CONF['pwd'],db=_CONF['db'])
    cursor = conn.cursor()
    yield cursor
    conn.commit()
    



def db_search_user(username):
    sql = "select * from personinfo where username = '%s'"%(username)
    cursor.execute(sql)
    results = cursor.fetchall()
    print (results)
    db.commit()