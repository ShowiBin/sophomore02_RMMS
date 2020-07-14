from datetime import timedelta
import datetime
from flask import Flask, render_template, request
# import numpy as np
import server

import model.USER_DBOP as user_OP
import model.BLOS_DBOP as blogs_OP
from model.Sql import SqlOp

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
python, Flask, numpy, javascript, html, css, maven, java, tomcat, spring, mysql, sqlite
<br>
V 20/7/3 使用说明：<br>
6.<br>
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


@app.route('/showTable', methods=['post', 'get'])
def showTable():
    obj = (request.args.get('obj'))
    cond = (request.args.get('cond'))
    print(cond)
    DB = SqlOp()
    # print(obj,cond)
    try:
        data = DB.select(obj,condition=cond)
        cols = DB.getCol(obj)
    except:
        data = 'ERROR'
        cols = 'ERROR'
    if obj == 'rcxc_info':
        return render_template('showTable.html',data=data,colnames = cols)
    elif obj == 'dqjcpzd_info':
        return render_template('showTable_dinqi.html',data=data,colnames = cols)
    else:
        return render_template('showTable.html',data=data,colnames = cols)

@app.route('/insertData', methods=['post', 'get'])
def insertData():
    obj = (request.args.get('obj'))
    data = eval((request.args.get('data')))
    DB = SqlOp()

    sql = '''
    insert into {} values ('''.format(obj)
    sql = sql+','.join(data.split(';'))[:-1]+')'
    #     sql=sql+i
    # sql = sql[:-2]+')'
    print(sql)
    try:
        # data = DB.select(obj,condition=cond)
        # cols = DB.getCol(obj)
        DB.runSql(sql)
        res = 1
    except:
        # data = 'ERROR'
        res = 0

    return str(res)


@app.route('/getCols', methods=['post', 'get'])
def getCols():
    data = False
    info=''
    obj = (request.args.get('obj'))
    try:
        data = eval((request.args.get('data')))
    except:
        print('no data')
    # print(data)
    DB = SqlOp()
    print('1')
    if data == True:
        cond = (request.args.get('cond'))
        print(cond)
        info = (DB.select(obj,condition=cond,flag=False))
        print(info)
        info = list(info)
        print(info)
        #处理返回的info中特殊的datetime数据类型

        for i, v in enumerate(info[0]):
            if 'int' not in str(type(v)):
                info[0][i] =  str(v)

    try:
        # data = DB.select(obj,condition=cond)
        cols = DB.getCol(obj)
    except:
        # data = 'ERROR'
        cols = 'ERROR'
    print(str([cols,info]))
    if data == True:
        return str([cols,info])
    else:
        return str(cols)

@app.route('/delData', methods=['post', 'get'])
def delData():
    obj = (request.args.get('obj'))
    cond = (request.args.get('cond'))
    DB = SqlOp()
    try:
        # data = DB.select(obj,condition=cond)
        print(obj,cond)
        DB.delete(obj,cond)
        res = 1
    except:
        # data = 'ERROR'
        res =0
        print(str(res))
    return str(res)


@app.route('/showPre', methods=['post', 'get'])
def showPre():
    cond = (request.args.get('cond'))
    s = SqlOp()
    data = s.select('dqjcsh_info','road_id='+cond.split('=')[-1])
    print(data)
    cols = ''
    datas=''
    for i in ['路面类型',
'起止位置',
'检查总长',
'检查总宽',
'损坏类型',
'损坏长',
'损坏宽',
'损坏高',
'损坏位置及损坏情况描述',
'损坏面积']:
        cols = cols + '<td>'+i+'</td>'
    for i in data[0][3:]:
        datas = datas+'<td>'+str(i)+'</td>'
    print(datas)
    return '''<div id="showPre" style="position:absolute;right : 0px;">
<table class="table table-bordered  table-hover table-success">
        <thead id="tableHead">
                '''+cols+'''
        </thead>

        <tbody>
                <tr>
                        '''+datas+'''
                </tr>
                    <td><button style="background-color: transparent;border-radius: 12px;" id='{{ raw[0] }}' onclick="hidePreB('{{ colnames[0]  }} ={{ raw[0] }}')" >收起</button></td>
                    <td><button style="background-color: transparent;border-radius: 12px;"  onclick="updatePre('{{ colnames[0]  }} ={{ raw[0] }}')" >修改</button></td>
                
        </tbody>
    </table>

</div>'''







if __name__ == '__main__':
    app.run()
