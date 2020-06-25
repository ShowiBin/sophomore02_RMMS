from model.Sql import SqlOp



def getNicknameByUsername(username):
    s = SqlOp()#s.select('USER','username like "Showi"')
    allData = s.select('USER','USERNAME is "{}"'.format(username))
    print('#USER_DBOP.getNicknameByUsername',allData)
    # nickname = allData[0][1]#!!!!!!!!!!!!!!!!!!!????
    nickname = 'undefined'
    for i in allData:
        if i[0] == username:
            nickname = i[1]
    return nickname

def login(username,pwd):
    s = SqlOp()
    users = s.select(table_name='USER')
    for i in users:
        print(i[0],i[2])
        if i[0] == username and i[2] == pwd:
            return str([{'isOk':1,'nickname':getNicknameByUsername(username)}])
    return str([{'isOk':0}])
def getNameByID(username):
    '''
    通过ID获得名字
    :param username:
    :return:
    '''
    s = SqlOp()
    users = s.select('USER')
    for i in users:
        if i[0] == username:
            return i[1]
    return 'Wrong'


def signup(username, pwd, name, age):
    if getNameByID(username)=='Wrong':
        s = SqlOp()# s.insert('USER',{'USERNAME':'Showi','NICKNAME':'Showi','PWD':'Showi666','AGE':'20'})
        s.insert('USER',{'USERNAME':username,'NICKNAME':name,'PWD':pwd,'AGE':age
        })
        return name
    return '0'