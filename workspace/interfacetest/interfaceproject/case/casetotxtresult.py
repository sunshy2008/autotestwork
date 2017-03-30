__author__ = 'Administrator'
__author__ = 'Administrator'
from openpyxl import load_workbook
from interfaceproject.papi import handlefunction
import json

testData1 = {'message': '服务器对时成功', 'success': 1, 'data': {'secrect': 'df525388', 'key': '225475478', 'UtcDiff': -5}}
'''
#打开excel表和sheet,将文件转换为json数据格式
wb = load_workbook('interfacetestdata.xlsx')
sheetNames = wb.get_sheet_names()
ws = wb.get_sheet_by_name(sheetNames[0])
rowNum = 2
testData2 = handlefunction.testdatadict(ws, rowNum)
'''
#打开json数据文件，取出数据
ff = open('data4.json', 'r', encoding='utf-8',)
testData2 = json.load(ff)

#将参数值写入接口字符串中
apiStr = testData2['apiStr']
strKey = '&key={key}'
strSec = '&sec={secrect}'
strSign = '&sign={sign}'
apiStrValue = handlefunction.apiStrReplaceValue(apiStr, testData2['inputparam'])
strKeyValue = handlefunction.apiStrReplaceValue(strKey, testData1['data'])
strSecValue = handlefunction.apiStrReplaceValue(strSec, testData1['data'])
#将字符串加密获取签名
strSignValue = strSign.replace('{sign}', str(handlefunction.strmd5(apiStrValue, strKeyValue, strSecValue)))
#拼接URL字符串
strUrl = testData2['url']+apiStrValue+strKeyValue+strSignValue
#写左侧列表txt文件（标题连接成一个字符串）
handlefunction.writeleftsidetxt(testData2)
# 将要发送的数据写入txt文件
handlefunction.writetxtsenddata(testData2)
#发送get请求，获取返回信息
resposedata=handlefunction.sendData(strUrl)
#判断返回结果与期望是否一致，并将结果写入txt文件
handlefunction.writetxtresult(testData2, resposedata)
