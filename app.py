from datetime import timedelta
import datetime
from flask import Flask, render_template, request

import server

import model.USER_DBOP as user_OP
import model.BLOS_DBOP as blogs_OP
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

timer = 0
@app.route('/')
def hello_world():
    global timer
    with open('log.txt', 'a') as f:
        f.write(str(timer)+'\n')
        f.write(str(datetime.datetime.now()))
        f.write('\n')
    timer += 1
    return render_template('home.html')


@app.route('/userPage')
def user():
    return '<h1>User page is still on construction</h1>'

@app.route('/home')
def p_home():
    global timer
    with open('log.txt', 'a') as f:
        f.write(str(timer)+'\n')
        f.write(str(datetime.datetime.now()))
        f.write('\n')
    timer += 1
    return render_template('home.html')


@app.route('/login', methods=['post', 'get'])
def p_login():
    return render_template('login.html')


@app.route('/signup')
def p_signup():
    return render_template('signup.html')


@app.route('/server', methods=['post', 'get'])
def s_data():
    data_name = eval(request.args.get('dataName'))
    data = server.DataGet()
    res = data.getData(data_name)
    print('res', res)
    return str(res)

@app.route('/serverLogin',methods=['post','get'])
def s_login():
    username = eval(request.args.get('username'))
    pwd = eval(request.args.get('pwd'))
    return user_OP.login(username,pwd)

@app.route('/serverSignUp',methods=['post','get'])
def s_signup():
    username = eval(request.args.get('username'))
    pwd = eval(request.args.get('pwd'))
    name = eval(request.args.get('name'))
    age = eval(request.args.get('age'))
    return user_OP.signup(username,pwd,name,age)

@app.route('/sorry',methods=['post','get'])
def sorry():
    return '''
        <h1>对不起，此功能还没实现呢</h1>
    '''
@app.route('/about',methods=['post','get'])
def about():
    return '''
        本项目由啦啦啦啦啦啦啦唐佳雪，杨泽来，张益劼，肖思瑶共同完成<br>
实现技术：<br>
python, Flask, numpy, javascript, html, css, maven, java, tomcat, spring, sqlServer, sqlite
<br>
参考：<br>
//Showi小冰 project:重庆交通大学表演部，https://github.com/ShowiBin/byb//我要不要写这个参考呢<br>
    '''
@app.route('/learn_more',methods=['post','get'])
def learn_more():
    return '''
    <style>
        background-color:gray;
    </style>
    <h1>LEARN MORE</h1>
        <a href='http://www.cqjtu.edu.cn/' style="text-decoration:none;color:gold;">重庆交通大学</a><br>
        <a href='http://sise.cqjtu.edu.cn/' style="text-decoration:none;color:gold;">重庆交通大学信息学院</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学数统学院</a><br>
        <a href='/sorry' style="text-decoration:none;color:gold;">重庆交通大学大学生校社联</a><br>
        <a href='http://www.showi.online' style="text-decoration:none;color:gold;">Showi小冰</a><br>
    '''

@app.route('/welcome',methods=['post','get'])
def welcome():
    '''
    show welcome html page
    :return:
    '''
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
