# -*- coding: utf-8 -*-
<<<<<<< HEAD
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kimhyoseong.db'
=======
from gtts import gTTS
from playsound import playsound
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///kimhyoseong.db'
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://id@비밀번호'
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
<<<<<<< HEAD
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
=======
    userid = db.Column(db.Integer, primary_key = True)
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))
    jicwi = db.Column(db.String(100))

    def __init__(self, username, email, tel, jicwi):
        self.username = username
        self.email = email
        self.tel = tel
        self.jicwi = jicwi

@app.route('/')
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
<<<<<<< HEAD
    return render_template("index.html", employees=all_data)
=======
    # return "hello flask"
    return render_template("index.html",employees=all_data)
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']
        jicwi = request.form['jicwi']

<<<<<<< HEAD
        insertUser = Employee(username,email,tel)
=======
        insertUser = Employee(username,email,tel,jicwi)
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
<<<<<<< HEAD
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
=======
    delUser = Employee.query.get(uid) #select * from Employee where userid=3
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee.query.get(request.form.get('userid'))
        updateUser.username = request.form['username']
<<<<<<< HEAD
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        updateUser.jicwi = request.form['jicwi']
        db.session.commit()
        return redirect(url_for('index'))

=======
        updateUser.email = request.form['email']   
        updateUser.tel = request.form['tel']
        updateUser.jicwi = request.form['jicwi']
        db.session.commit()
        
        return redirect(url_for('index'))
    
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
<<<<<<< HEAD
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

=======
    return render_template("index.html",employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월20일 입니다. 고양이가 소리를 내려고합니다. 우리 모두 스마트고양이를 응원합시다."
    filename = "hellosmartcat.mp3"
    tts=gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)
>>>>>>> 253bfffe79d1ab86136ae886bf93f7cd62b9ea62
    return "고양이가 소리를 냈습니다."