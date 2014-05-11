# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

#coding:utf-8
from flask import Flask

app = Flask(__name__)
# app.config.from_pyfile('config.cfg')   #导入配置文件
app.config.from_object('config')

import view
from data import *

if __name__ == '__main__':
    db.create_all()
    app.run()