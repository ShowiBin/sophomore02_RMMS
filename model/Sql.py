import sqlite3


class SqlOp():
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