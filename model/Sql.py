import pymysql


class SqlOp():
    '''这个模块用来管理数据库
    数据库使用sqlite
    所有的有关sqlite3的数据操作，在本package中执行，所用的数据库才是同一个
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
            colums.append(self.dataTrans(i[0]))
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


    def dataTrans(self,data):
        transTable = {'road_id': '道路编码',
                      'user_no': '检查人员',
                      'rcxc_rq': '日常检查日期',
                      'rcxc_shlx': '本次损坏类型',
                      'rcxc_shwz': '损坏情况',
                      'rcxc_bz': '备注'
                      }
        try:
            return transTable[data]
        except:
            return data

# s = SqlOp()
#
# s.insert('USER',{'ID':'631862020224','NAME':'Showi','YEAR':'2018','PWD':'Showi666','CONMENTS':'管理员'})
# # s.update('USER','NAME','Showi'," ID = '631862020224'")
# s.delete('USER','ID = 22')
# print(s.select('USER'))



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

