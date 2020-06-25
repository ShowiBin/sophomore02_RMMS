from model import Sql


def addAttendence():
    '''
    这个模块的函数只能在数据库所在的dir下使用！！！！！！！！！
    :return:
    '''
    data = []
    time = input('TIME:')
    for i in range(14):#本初应该为成员树木
        data.append(input(i))

    s = Sql.SqlOp()
    s.insert('ATTENDENCE',{
    'TIMER':time,
    'ONE':data[0],
    'TWO':data[1],
    'THREE':data[2],
    'FOUR':data[3],
    'FIVE':data[4],
    'SIX':data[5],
    'SEVEN':data[6],
    'EIGHT':data[7],
    'NIGH':data[8],
    'TEN':data[9],
    'ELEVEN':data[10],
    'THIRTEEN':data[11],
    'TWELVE':data[12],
    'FORTEEN':data[13],
                           })



def addAccounting():
    '''
    怎加账单
    这个模块的函数只能在数据库所在的dir下使用！！！！！！！！！
    :return:
    '''
    data = []
    time = input('TIME:')
    reason = input('REASON:')
    person = input('PERSON:')
    inorout = input('INOROUT:')
    remain = input('REMAIN:')
    comments = input('COMMENTS:')

    s = Sql.SqlOp()

    s.insert('MONEY',{'TIME':time,'REASON':reason,'PERSON':person,'INOROUT':inorout,'REMAIN':remain,'CONMENTS':comments})


