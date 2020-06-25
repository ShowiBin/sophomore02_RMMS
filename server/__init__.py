
import sqlite3
import requests
from bs4 import BeautifulSoup
import model.Sql as Sql

import model.Sql as sql


class DataGet():
    def __init__(self):
        pass
    def getBlogsData(self):
        '''Get the blogs.html data'''
        data = []
        s = sql.SqlOp()
        count = s.runSql('select count(*) from BLOGS')[0][0]
        startCol = count - 15
        data = s.select('BLOGS', 'id > ' + str(startCol))
        copy = []
        for i in data:
            copy.append(list(i))
        return str(copy).replace('None','"*"')


    def getAppdata(self):
        '''
        get app data
        :return: a json data,can be parse to a list,caontain obj consisting of img,href,name
        '''
        url = 'https://m.wandoujia.com/top/app'
        html = requests.get(url).text#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1.获取网页所有的html

        soup = BeautifulSoup(html,"html.parser")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!2.使用bs4将html解析
        i = 0
        imgs = []
        href = []
        names = []
        for tag in soup.find_all('div', class_='icon-wrap'):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!3.找到其中的类名为icon-wrap的div的内容
            if i > 30:
                break
            href.append(tag.find('a').get_attribute_list('href'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!4.获取网页中的标签为a的属性:href
            imgs.append(tag.find('img').get_attribute_list('src'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            names.append(tag.find('img').get_attribute_list('alt'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            i = i+1
        data = []
        for img,hr,name in zip(imgs,href,names):
            obj = {}
            obj['img'] = img
            obj['href'] = hr
            if len(name[0]) > 5:
                nameShort = name[0][:4]+'...'
                obj['name'] = nameShort
                # print('a')
            else:
                obj['name'] = name
            data.append(obj)
        return str(data)

    def getNewsData(self):
        '''

        :return:
        '''

        url = 'http://tech.123.com.cn/ai/'
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")
        i = 0
        html = []
        for tag in soup.find_all('li', class_='hasimg'):
            if i > 5:
                break
            html.append(i)

            i = i + 1
        return str(html)

    def getEvents(self):
        '''Get the events.html data'''
        data = []
        s = sql.SqlOp()
        count = s.runSql('select count(*) from EVENTS')[0][0]
        startCol = count - 15
        data = s.select('EVENTS', 'id > ' + str(startCol))
        copy = []
        for i in data:
            copy.append(list(i))
        return str(copy).replace('None', '"*"')

    def getAttendence(self):
        '''Get the events.html data'''
        data = []
        s = sql.SqlOp()
        data = s.select('ATTENDENCE')
        copy = []
        for i in data:
            copy.append(list(i))
        return str(copy).replace('None', '"*"')

    def getMoney(self):
        '''Get the money.html data'''
        data = []
        s = sql.SqlOp()
        data = s.select('MONEY')
        copy = []
        for i in data:
            copy.append(list(i))
        return str(copy).replace('None', '"*"')

    def getData(self, data_name):
        '''get data by the request'''
        if(data_name == 'homeBlogData'):
            # print('#server.init.getData:','yo')
            return self.getBlogsData()
        elif(data_name=='app'):
            return self.getAppdata()
        elif(data_name=='events'):
            return self.getEvents()
        elif(data_name=='news'):
            return self.getNewsData()
        elif(data_name=='attendence'):
            return self.getAttendence()
        elif(data_name=='money'):
            return self.getMoney()


#
# a = DataGet()
# obj = eval(a.getData('news'))
# print(obj)



