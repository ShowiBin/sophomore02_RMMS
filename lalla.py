import model.Sql as Sql
import server as se
from model import UsefulFunc

# s = Sql.SqlOp()
# s.insert('MONEY',{'TIME':'2020.10.01','REASON':'出席双福国庆晚会','PERSON':'ALL members','INOROUT':'+1000','REMAIN':'1099'})
# for i in s.select('MONEY'):
#     print(i)
# print(s.runSql('select  from USER'))
# count = s.runSql('select count(*) from BLOGS')[0][0]
# startCol = count - 15
# for i in s.select('BLOGS','id > '+str(startCol)):
#     print(i)
# s.insert('BLOGS',{'TITLE':'Showi小冰:每一个爱笑的灵魂背后都是一个..giao?','CON':'一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao'})
# s.runSql('''create table EVENTS(#//=================================
# ID TEXT NOT NULL  ,
# NICKNAME TEXT NOT NULL,
# PWD TEXT NOT NULL,
# AGE TEXT NOT NULL,
# CONMENTS TEXT)
#''')#//=============================================================
# s.insert('USER',{'USERNAME':'Showi','NICKNAME':'Showi','PWD':'123123','AGE':'20'})

# :param table_name: 数据库的名字
#         :param kwargs: 可变参长度的参数,字典形式传入
# print(s.runSql("SELECT name _id FROM sqlite_master WHERE type ='table'"))
# s.runSql('drop table BLOGS')
# s.insert('BLOGS',{'TITLE':'Showi小冰:每一个爱笑的灵魂背后都是一个..giao?','CON':'一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao一给我力giaogiao'})


# s.runSql('''create table MONEY(
# ID integer primary key autoincrement,
# TIME TEXT NOT NULL,
# REASON TEXT NOT NULL,
# PERSON TEXT NOT NULL,
# INOROUT TEXT NOT NULL,
# REMAIN TEXT NOT NULL,
# CONMENTS TEXT)
# ''')
#


UsefulFunc.addAccounting()
