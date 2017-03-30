__author__ = 'Administrator'
import hashlib
import json

import requests

from interfaceproject.papi import handleexcel07



#读取excel表中一行数据，转换为字典格式
def testdatadict(ws,rownum):
    data_dic = {}
    for columnnum in range(1,len(ws[1])+1):
        cellkey = ws.cell(row=1, column=columnnum).value
        if ws.cell(row=rownum, column=columnnum).value.find('{"') == 0:
            cellvalue = json.loads(ws.cell(row=rownum, column=columnnum).value)
        else:
            cellvalue = ws.cell(row=rownum, column=columnnum).value
        data_dic[cellkey] = cellvalue
    return data_dic
#发送请求，并将请求的数据和请求的响应结果写到txt文件中
def sendData(strUrl):
    # 发送请求
    data = requests.get(strUrl)
    return data
#写左侧列表数据到txt（读取生成html报告时使用）
def writeleftsidetxt(testData):
    #发送数据获取
    payload = {}
    # 从json中获取发送参数
    for x in testData["inputparam"].items():
        payload[x[0]] = x[1]
    with open('leftside.txt', 'a+', encoding='utf-8') as f:
        f.write(testData['TestId'])
        f.write('-')
        f.write(testData['Title'])
        f.write('\n')
def wirteexcelresult(testData, resultdata, filename, rownum):
    r = resultdata.json()
    wr = handleexcel07.Write_excel(filename)
    for x in range(1,11):
        for y in testData.items():
            if y[0]==wr.pvalue(1,x):
                wr.write(rownum,x,y[1])
    for x in range(1,11):
        for y in r.items():
            if y[0]==wr.pvalue(1,x):
                wr.write(rownum,x,str(y[1]))
    try:
        if str(r['success']) == testData['Result']['flag_success']:
            wr.write(rownum, 6, 'pass')
        else:
            wr.write(rownum, 6, 'fail')
    except Exception:
        wr.write(rownum, 6, 'no except result')

def writetxtresult(testData, data):
    r = data.json()
    with open('result.txt', 'a+', encoding='utf-8') as rst:
        rst.write('return data')
        rst.write('|')
        for x in r.items():
            rst.write(x[0])
            rst.write(':')
            rst.write(str(x[1]))
            rst.write('|')
        try:
            if str(r['success']) == testData['Result']['flag_success']:
                rst.write('pass')
            else:
                rst.write('fail')
        except Exception:
            rst.write('no except result')
        rst.write('\n')

#发送数据写入文件
def writetxtsenddata(testData):
    with open('rightside.txt', 'a+', encoding='utf-8') as rs:
        rs.write('发送数据')
        rs.write('|')
        rs.write('标题:'+testData['Title'])
        rs.write('|')
        rs.write('发送方式:'+testData['Method'])
        rs.write('|')
        rs.write('案例描述:'+testData['Desc'])
        rs.write('|')
        rs.write('发送地址:'+testData['url'])
        rs.write('|')
        rs.write('接口:'+testData['apiStr'])
        rs.write('|')
        rs.write('发送参数:'+str(testData['inputparam']))
        rs.write('|')
        rs.write(testData['TestId'])
        rs.write('\n')

#将接口中的参数替换为测试案例中的值
def apiStrReplaceValue(strpara,dataPara):
    for x in dataPara.items():
        strold = str('{'+x[0]+'}')
        strnew = str(x[1])
        strpara = strpara.replace(strold, strnew)
    return strpara
#对发送的请求根据key和秘钥进行MD5加密
def strmd5(apiStrValue, strKeyValue='', strSecValue=''):
    strmd5 = apiStrValue+strKeyValue+strSecValue
    m3 = hashlib.md5()
    m3.update(strmd5.encode('utf-8'))
    return m3.hexdigest()

