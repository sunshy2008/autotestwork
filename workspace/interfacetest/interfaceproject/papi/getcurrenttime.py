__author__ = 'Administrator'
import hashlib
import json
import time
import requests
ssa ={'message': '服务器对时成功', 'success': 1, 'data': {'secrect': 'df525388', 'key': '225475478', 'UtcDiff': -5}}
ff =open('data2.json', 'r', encoding='utf-8',)
testData2 = json.load(ff)
payload = {}
for x in testData2["inputparam"].items():
    payload[x[0]] = x[1]
print(payload)
testData2['inputparam']['ts']=int(time.time())
strforsign1 = testData2['api_str']+'?appID='+str(testData2['inputparam']['appID'])+ '&appVersion='+str(testData2['inputparam']['appVersion'])+'&ver='+str(testData2['inputparam']['ver'])
strforsign2 = '&ts='+str(testData2['inputparam']['ts'])
strforsign3 = '&key='+str(ssa['data']['key'])
strforsign4 = '&sec='+str(ssa['data']['secrect'])
strforsign =strforsign1+strforsign2+strforsign3+strforsign4
print(strforsign)
m3 = hashlib.md5()
m3.update(strforsign.encode('utf-8'))
print(type(m3.hexdigest()))
strforsign5 = '&sign='+m3.hexdigest()
Url=testData2['url']+strforsign1+strforsign2+strforsign3+strforsign5
Ur2=testData2['url']+testData2['api_str']
print(Url)
data = requests.get(Ur2,params=payload)
r = data.json()
print(r)
print(data)
