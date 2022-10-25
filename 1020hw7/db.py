# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:50:31 2022

@author: user
"""

import  pymysql

dbsetting = {
    "host":"127.0.0.1",
    'port':3306,
    'user':'root',
    'password':'123456789',
    'db':'jobs',
    'charset':'utf8'
    }

conn=pymysql.connect(**dbsetting)