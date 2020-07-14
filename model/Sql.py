import sqlite3

import pymysql


class SqlOp():
    '''这个模块用来管理数据库
    使用的是mysql
    所有的有关mysql的数据操作，在本package中执行，所用的数据库才是同一个
    '''

    def getCon(self, DB_name='RMMS_MAIN'):
        '''连接到指定的db'''
        con = pymysql.connect(
            host='cdb-eb41x5xk.cd.tencentcdb.com',
            port=10060,
            user='root',
            password='showi666',
            database='RMMS',
            charset='utf8'
        )
        return con


    def runSql(self, sql):
        '''
        直接运行要运行的sql语句，可获取返回值
        :param sql: slq语句
        :return: 返回的参数啥的
        '''
        print(sql)
        con = self.getCon()
        c = con.cursor()
        c.execute(sql)
        res = c.fetchall()
        # print(res)
        if 'select' in sql:

            data = []
            for row in res:
                data.append(list(row))
            con.commit()
            con.close()
            return data
        else:
            con.commit()
            con.close()
            print('#[model.Sql.SqlOp.runSql]#excute success')
    def getCol(self,table):
        '''get all the cols name'''
        c = self.getCon()
        con = c.cursor()
        con.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = '"+table+"'")
        cols = con.fetchall()
        colums = []
        # print(cols,cols[0],cols[0][0],type(cols[0]))
        for i in cols:
            colums.append(self.en2cn(i[0]))
        return colums

    def insert(self, *args, **kwargs):
        '''
        网数据库insert数据,
        :param table_name: 数据库的名字
        :param kwargs: 可变参长度的参数,字典形式传入
        :return:
        '''
        table_name = args[0]
        kwargs = args[-1]
        print(table_name)
        print(kwargs,type(kwargs))
        keys = ''
        values = ''
        for key, value in kwargs.items():
            keys += ("'"+key+"'"+',')
            values += ("'"+value+"'" + ',')
        keys = keys[:-1]
        values = values[:-1]
        sql = '''insert into ''' + table_name + '''(''' + keys + ''') values (''' + values + ''')'''
        print(sql)
        self.runSql(sql)

    def delete(self,tabel_name,condition):
        '''
        删除表中数据
        :param tabel_name:str
        :param condition:str True or 'ID' = '23213'
        :return:
        '''
        condition = condition.replace(' ','')
        condition_ = self.cn2en(condition.split('=')[0])+'='+condition.split('=')[1]
        sql = 'delete from '+tabel_name+' where '+condition_
        self.runSql(sql)

    def update(self,tabel_name,col,newdata,condition):
        '''
        更新表
        like : update('USER','ID','213213','ID' = 123)
        :param tabel_name: str
        :param col: str
        :param newdata:str
        :param condition: str like '1 >0 ' or 'ID = '6318'
        :return: None
        '''
        sql = '''update {} set '{}' = '{}' where {} '''.format(tabel_name,col,newdata,condition)
        print('#[model.Sql.SqlOp.update]',sql)
        self.runSql(sql)

    def select(self,table_name,condition = None,flag = True):
        '''
        为了方便，我直接把所有的都返回了.......0.0
        //2020/7/9 我是西安了模糊查询，并所有的查询都是模糊插叙
        :param table_name: str
        :return:返回一个包含所有信息的数据

        '''
        if not condition:
            condition_ = 'True'
        else:
            condition = condition.replace(' ', '')
            condition_ = self.cn2en(condition.split('=')[0]) + '=' + condition.split('=')[1]
            if table_name != 'dqjcsh_info' and flag:
                condition_ = condition_.replace('=',' like ')
                condition_ = condition_[:-1]+"%'"
                condition_ = condition_.replace("'","'%")[:-1]
        sql = 'select * from '+table_name+' where '+condition_
        print('#[model.Sql.SqlOp.select]',sql)
        return self.runSql(sql)

    def cn2en(self,cn):
        '''中文转化为英文'''
        transTable = { '道路编码': 'road_id',
                       '检查人员': 'user_no',
                       '日常检查日期': 'rcxc_rq',
                       '本次损坏类型': 'rcxc_shlx',
                       '损坏情况': 'rcxc_shwz',
                       '备注(日常检查)':'rcxc_bz',
                       '定期检查日期':'sh_rq',
                       '路面类型':'sh_lmlx',
                       '道路编号':'sh_dlbh',
                       '平整度指数(IRI)':'pzd_IRI',
                       '备注(定期检查)':'pzd_bz',
                        '起止位置':'sh_qzwz',
                        '检查总长':'sh_jczc',
                        '检查总宽':'sh_jczk',
                        '损坏类型':'sh_shlx',
                        '损坏长':'sh_shc',
                        '损坏宽':'sh_shk',
                        '损坏高':'sh_shg',
                        '损坏位置以及损坏情况':'sh_shwz',
                        '损坏面积':'sh_shmj'
                      }
        try:
            return transTable[cn]
        except:
            return cn






    def en2cn(self,en):
        '''英文转化为中文'''
        transTable = {'road_id': '道路编码',
                      'user_no': '检查人员',
                      'rcxc_rq': '日常检查日期',
                      'rcxc_shlx': '本次损坏类型',
                      'rcxc_shwz': '损坏情况',
                      'rcxc_bz': '备注(日常检查)',
                      'sh_rq':'定期检查日期',
                     'sh_lmlx':'路面类型',
                     'sh_dlbh':'道路编号',
                     'pzd_IRI':'平整度指数(IRI)',
                     'pzd_bz':'备注(定期检查)',
                      'sh_qzwz':'起止位置',
                     'sh_jczc':'检查总长',
                     'sh_jczk':'检查总宽',
                     'sh_shlx':'损坏类型',
                     'sh_shc':'损坏长',
                     'sh_shk':'损坏宽',
                     'sh_shg':'损坏高',
                     'sh_shwz':'损坏位置以及损坏情况',
                     'sh_shmj':'损坏面积'
                      }
        try:
            return transTable[en]
        except:
            return en

class SqlOp2():
    '''这个模块用来管理数据库
    数据库使用sqlite
    所有的有关sqlite3的数据操作，在本package中执行，所用的数据库才是同一个
    '''

    def getCon(self, DB_name='DB_for_DepartmentManager.db'):
        '''连接到指定的db'''
        con = sqlite3.connect(DB_name)
        return con

    def runSql(self, sql):
        '''
        直接运行要运行的sql语句，可获取返回值
        :param sql: slq语句
        :return: 返回的参数啥的
        '''
        con = self.getCon()
        c = con.cursor()
        res = c.execute(sql)

        if 'select' in sql:
            data = []
            for row in res:
                data.append(row)
            con.commit()
            con.close()
            return data
        else:
            con.commit()
            con.close()
            print('#[model.Sql.SqlOp.runSql]#excute success')

    def insert(self, *args, **kwargs):
        '''
        网数据库insert数据,
        :param table_name: 数据库的名字
        :param kwargs: 可变参长度的参数,字典形式传入
        :return:
        '''
        table_name = args[0]
        kwargs = args[-1]
        print(table_name)
        print(kwargs,type(kwargs))
        keys = ''
        values = ''
        for key, value in kwargs.items():
            keys += ("'"+key+"'"+',')
            values += ("'"+value+"'" + ',')
        keys = keys[:-1]
        values = values[:-1]
        sql = '''insert into ''' + table_name + '''(''' + keys + ''') values (''' + values + ''')'''
        print(sql)
        self.runSql(sql)

    def delete(self,tabel_name,condition):
        '''
        删除表中数据
        :param tabel_name:str
        :param condition:str True or 'ID' = '23213'
        :return:
        '''
        sql = 'delete from '+tabel_name+' where '+condition
        self.runSql(sql)

    def update(self,tabel_name,col,newdata,condition):
        '''
        更新表
        like : update('USER','ID','213213','ID' = 123)
        :param tabel_name: str
        :param col: str
        :param newdata:str
        :param condition: str like '1 >0 ' or 'ID = '6318'
        :return: None
        '''
        sql = '''update {} set '{}' = '{}' where {} '''.format(tabel_name,col,newdata,condition)
        print('#[model.Sql.SqlOp.update]',sql)
        self.runSql(sql)

    def select(self,table_name,condition = None):
        '''
        为了方便，我直接把所有的都返回了.......0.0
        :param table_name: str
        :return:返回一个包含所有信息的数据
        '''
        if not condition:
            condition = 'True'
        sql = 'select * from '+table_name+' where '+condition
        print('#[model.Sql.SqlOp.select]',sql)
        return self.runSql(sql)
# s = SqlOp()

# s.insert('USER',{'ID':'631862020224','NAME':'Showi','YEAR':'2018','PWD':'Showi666','CONMENTS':'管理员'})
# s.update('USER','NAME','Showi'," ID = '631862020224'")
# s.delete('USER','ID = 22')
# print(s.select('dqjcsh_info','road_id=2')[0])



# s = SqlOp()
# s.runSql('''create table USER(
# ID TEXT NOT NULL ,
# NAME TEXT NOT NULL,
# PWD TEXT NOT NULL,
# YEAR TEXT NOT NULL,
# CONMENTS TEXT)
# ''')

# DB = SqlOp()
# obj='rcxc_info'
# cond = None
# data = DB.select(obj,condition=cond)
# cols = DB.getCol(obj)

