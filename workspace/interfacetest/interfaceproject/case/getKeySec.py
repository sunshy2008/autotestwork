__author__ = 'Administrator'
import json
from openpyxl import load_workbook
from interfaceproject.papi import handlefunction
testData1 = {'message': '服务器对时成功', 'success': 1, 'data': {'secrect': 'df525388', 'key': '225475478', 'UtcDiff': -5}}
#打开excel表和sheet,将文件转换为json数据格式
wb = load_workbook('interfacetestdata.xlsx')
sheetNames = wb.get_sheet_names()
ws = wb.get_sheet_by_name(sheetNames[0])
rowNum = 2
testData2 = handlefunction.testdatadict(ws, rowNum)
#将参数值写入接口字符串中
apiStr = testData2['apiStr']
apiStrValue = handlefunction.apiStrReplaceValue(apiStr, testData2['inputparam'])
#拼接URL字符串
strUrl = testData2['url']+apiStrValue
#发送get请求，获取返回信息
resposedata= handlefunction.sendData(strUrl)
if resposedata.json():
    r = resposedata.json()
    with open('DataKeyAndSec.json', 'w', encoding='utf-8') as f:
        json.dump(r, f, ensure_ascii=False,indent=4)
    #判断返回结果与期望是否一致，并将结果写入txt文件
    filename = 'interfaceresult.xlsx'
    handlefunction.wirteexcelresult(testData2, resposedata, filename, rowNum)
