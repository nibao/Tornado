#!/usr/bin/env Python
# coding=utf-8
import os
import configparser

import tornado.ioloop
from tornado.web import Application

import sys
sys.path.append('../')
from Tornado.db import init_db
from Tornado.url import URL

#读取developers.config文件
def parse_config():
    #获取config文件
    #os.environ为环境变量的字典，APP_CONF为对应文件的环境变量名称，通过get取值
    conf_file = os.environ.get('APP_CONF')
    #configparser读取配置文件的方法，不过需要先实例化为ConfigParser对象
    conf = configparser.ConfigParser()
    conf.read(conf_file)
    return conf

def make_app(conf):
    app = Application(URL)
    port = conf.getint('main','port')
    app.listen(port)

    app.settingss['jwt_priv_key'] = conf['main'][]
    return app


def main():
    conf = parse_config()
    db_conf = conf['db']
    init_db({
        "host": db_conf['host'],
        "user": db_conf['user'],
        "pwd": db_conf['password'],
        "db": db_conf['name']
    })

    APP = make_app(conf)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()