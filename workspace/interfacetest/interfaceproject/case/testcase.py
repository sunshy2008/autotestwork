__author__ = 'Administrator'

from openpyxl import load_workbook
from interfaceproject.papi import handlefunction
import time

testData1 = {'message': '服务器对时成功', 'success': 1, 'data': {'secrect': 'df525388', 'key': '225475478', 'UtcDiff': -5}}
#打开excel表和sheet,将文件转换为json数据格式
wb = load_workbook('interfacetestdata.xlsx')
sheetNames = wb.get_sheet_names()
ws = wb.get_sheet_by_name(sheetNames[0])
rowNum = 3
testData2= handlefunction.testdatadict(ws, rowNum)
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
#发送get请求，获取返回信息
timeStart = time.time()
resposedata= handlefunction.sendData(strUrl)
timeEnd = time.time()
print(timeEnd-timeStart)
#判断返回结果与期望是否一致，并将结果写入excel文件
filename = 'interfaceresult.xlsx'
handlefunction.wirteexcelresult(testData2, resposedata, filename, 5)
