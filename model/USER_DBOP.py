from model.Sql import SqlOp2



def getNicknameByUsername(username):
    s = SqlOp2()#s.select('USER','username like "Showi"')
    allData = s.select('USER','USERNAME is "{}"'.format(username))
    print('#USER_DBOP.getNicknameByUsername',allData)
    # nickname = allData[0][1]#!!!!!!!!!!!!!!!!!!!????
    nickname = 'undefined'
    for i in allData:
        if i[0] == username:
            nickname = i[1]
    return nickname




def getNikenameRIGHTByUsername(username):
    s = SqlOp2()  # s.select('USER','username like "Showi"')
    allData = s.select('USER', 'USERNAME is "{}"'.format(username))
    print('#USER_DBOP.getNicknameByUsername', allData)
    # nickname = allData[0][1]#!!!!!!!!!!!!!!!!!!!????
    nickname = 'undefined'
    for i in allData:
        if i[0] == username:
            nickname = i[1]
            RIGHT = i[2]
    return nickname,RIGHT


def login(username,pwd):
    s = SqlOp2()
    users = s.select(table_name='USER')
    for i in users:
        print(i[0],i[3])
        if i[0] == username and i[3] == pwd:
            nikname,RIGHT = getNikenameRIGHTByUsername(username)
            return str([{'isOk':1,'nickname':nikname,'RIGHT':RIGHT}])
    return str([{'isOk':0}])
def getNameByID(username):
    '''
    通过ID获得名字
    :param username:
    :return:
    '''
    s = SqlOp2()
    users = s.select('USER')
    for i in users:
        if i[0] == username:
            return i[1]
    return 'Wrong'


def signup(username, pwd, name, age):
    if getNameByID(username)=='Wrong':
        s = SqlOp2()# s.insert('USER',{'USERNAME':'Showi','NICKNAME':'Showi','PWD':'Showi666','AGE':'20'})
        s.insert('USER',{'USERNAME':username,'NICKNAME':name,'PWD':pwd,'AGE':age
        })
        return name
    return '0'