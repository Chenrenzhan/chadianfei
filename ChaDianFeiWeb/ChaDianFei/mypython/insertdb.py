#!/usr/bin/python
#encoding=utf-8

import sys

import MySQLdb

reload(sys)

sys.setdefaultencoding('utf-8')

class Insertdb(object):
    '''向数据库插入数据'''
    def __init__(self, dorm, mail):
        self.dorm = dorm
        self.mail = mail
        
    def save(self):
        con= MySQLdb.connect(host='localhost',user='root',passwd='crz332066279',db='chadianfeidb',charset='utf8')

        cursor =con.cursor()

        sql ="INSERT INTO chadianfei_chadianfei(dorm, mail) VALUES('%s', '%s')"%(self.dorm, self.mail)

        ret=cursor.execute(sql)
        con.commit()
        cursor.close()

        con.close()
