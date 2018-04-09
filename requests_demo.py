#coding=utf-8
import requests
payload = {'page':1, 'pageSize':10,'keyword':'大咖汇'}
#payload.encode = "utf-8"
re = requests.post("http://point.edujia.com/point/poster/search/ios/query/list.do",data=payload)
re.encoding='utf-8'
# point/poster/search/ios/query/list.do
print(re.headers)