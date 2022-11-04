# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:56:10 2022

@author: user
"""

from flask import Flask,render_template,request,url_for,redirect

import db


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/product',methods=['GET'])
def drink():
    item = request.args.get('click')
    
    if item == None:
        sql="select photo,chname,enname from drink"
    
    else:
        sql = "select photo,chname,enname from drink where typeid='{}'".format(item)
        
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchall()

    return render_template("product.html",result=res)        

@app.route('/news')
def news():
    sql = "select title,content from news"
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchall()
    
    return render_template("news.html",result=res)



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/addmessage',methods=['POST'])
def addcontact():
    if request.method == 'POST':
        username=request.form.get('username')
        email= request.form.get('email')
        subject=request.form.get('subject')
        content=request.form.get('content')
        
        sql = "insert into message(username,email,subject,content) values('{}','{}','{}','{}')".format(username,email,subject,content)
        
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        
    return redirect(url_for('contact'))
        
        
        
        
        
        



app.run(debug=True,host='0.0.0.0',port=5555)