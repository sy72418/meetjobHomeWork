# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:58:30 2022

@author: user
"""

import db

a = input('請輸入數字代碼(1 新增員工資料  2 新增工作項目  3 修改員工資料  4 查詢員工資料  5 查詢員工工作項目)：')

if a=='1':
    name=input('請輸入員工姓名：')
    sex=input('請輸入員工性別(F/M)：')
    tel = input('請輸入員工電話：')
    assume = input('請輸入就職日期(yyyy-mm-dd)：')
    
    sql="insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}') ".format(name,sex,tel,assume)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
elif a=='2':
    items = input('請輸入工作項目：')
    info = input('請輸入工作內容說明：')
    emid = input('請輸入負責項目的員工編號：')
    
    sql="insert into works(items,info,employeeid) values('{}','{}','{}')".format(items,info,emid)
    
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()

elif a=='3':
    b = input('請輸入欲修改的員工編號：')
    sql="select name,sex,tel from employee where id='{}'".format(b)
    
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    info = cursor.fetchall()
    
    for row in info:
        print('員工姓名：',row[0])
        print('性別：',row[1])
        print('電話：',row[2])
        print()
    
    c = input('請輸入欲修改的資料欄位代碼(1  電話  2 性別  3 電話及性別)：')
    
    if c=='1':
        d=input('請輸入更新的電話號碼：')
        sql = "update employee set tel='{}' where id='{}'".format(d,b)
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        print('已修改')
              
    elif c=='2':
        ns=input('請輸入更新的性別(F/M)：')
        sql = "update employee set sex='{}' where id='{}'".format(ns,b)
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        print('已修改')
        
    elif c=='3':
        d=input('請輸入更新的電話號碼：')
        ns=input('請輸入更新的性別(F/M)：')
        sql = "update employee set tel='{}',sex='{}' where id='{}'".format(d,ns,b)
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        print('已修改')
        
    else:
        print('無此代碼！')
        
elif a=='4':
    b=input('請輸入欲查詢的員工編號：')
    sql="select name,sex,tel,assume from employee where id='{}'".format(b)
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    info = cursor.fetchall()
    
    for row in info:
        print('員工姓名：',row[0])
        print('性別：',row[1])
        print('電話：',row[2])
        print('就職日期：',row[3])
        print()

elif a=='5':
    b=input('請輸入欲查詢的員工編號：')
    sql="select em.name,w.items,w.info from employee em join works w on em.id = w.employeeid where em.id='{}'".format(b)
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    info = cursor.fetchall()
    
    for row in info:
        print('員工姓名：',row[0])
        print('工作項目：',row[1])
        print('工作內容說明：',row[2])
        print()

else:
    print('輸入代碼錯誤')
    
    
    
    