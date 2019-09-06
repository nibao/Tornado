#!/usr/bin/env Python
# coding=utf-8
from url import URL
import tornado.web
import sys
sys.path.append('../')
import TornadoTest.db as mysqldb

adduser = mysqldb.db_create_table('person')

app = tornado.web.Application(URL)