#coding=gb2312
from flask import Flask
from flask import request
import json
import mysql


app = Flask(__name__)
#每页显示数
pageCount = 20

@app.route('/')
def start():
    return 'This is iCCUT Server!'


@app.route('/iCCUT/MediaList', methods=['POST','GET'])
def getMediaList():

    db = mysql.Mysql()

    try:
        index = request.args.get('index')
        leve1 = request.args.get('leve1')
        leve2 = request.args.get('leve2')

        result = []

        pageIndex = int(pageCount) * int(index)

        if leve2 == "":
            sql = 'select title,url from FreeVideo where leve1="%s" limit %s,%s' % (leve1,pageIndex,pageCount)
        else:
            sql = 'select title,url from FreeVideo where leve2="%s" limit %s,%s' % (leve2,pageIndex,pageCount)

        db.queryData(sql=sql)

        result_mysql = db.cur.fetchall()

        for item in  result_mysql:
            ji = {"title": item[0],"url":item[1]}
            result.append(ji)

        db.conn.close()

        if len(result) == 0:
            return getBaseReturnValue(data=result,msg="没有更多数据!",code=False)
        else:
            return getBaseReturnValue(data=result,msg='OK',code=True)

    except KeyError,e:
        print(e)
        return getBaseReturnValue(data=[],msg="Error",code=False)


@app.route('/iCCUT/NewsList', methods=['POST','GET'])
def getNewsList():

    db = mysql.Mysql()

    try:
        index = request.args.get('index')

        pageIndex = int(pageCount) * int(index)

        sql = 'select title,time,url from FreeNews order by time desc limit %s,%s' % (pageIndex,pageCount)

        db.queryData(sql)
        result_mysql = db.cur.fetchall()

        result = []

        for item in result_mysql:
            result.append({"title":item[0],"time":item[1],"url":item[2]})

        db.conn.close()

        if len(result) == 0:
            return getBaseReturnValue(data=result,msg="没有更多数据!",code=False)
        else:
            return getBaseReturnValue(data=result,msg='OK',code=True)

    except KeyError,e:
        return getBaseReturnValue(data=[],msg="Error",code=False)


@app.route('/iCCUT/SearchList', methods=['POST','GET'])
def getSearchList():

    db = mysql.Mysql()

    try:
        keyword = request.args.get('keyword')

        sql = "select title,url from FreeVideo where title like '%"+ keyword +"%' limit 0,20"

        db.queryData(sql)
        result_mysql = db.cur.fetchall()
        result = []
        for item in result_mysql:
            result.append({"title":item[0],"url":item[1]})

        db.conn.close()

        return getBaseReturnValue(data=result,msg='OK',code=True)
    except KeyError,e:
        return getBaseReturnValue(data=[],msg="Error",code=False)

def getBaseReturnValue(data,msg,code):
    json_data = json.dumps({'datas':data,'msg':msg,'success':code},ensure_ascii=False,encoding='gb2312')
    return json_data


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')