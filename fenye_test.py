# coding=UTF-8
from json import *
import clipboard

def htmlEscape(input) :
        if not input:
            return input
        input = input.replace("&", "&amp;")
        return input
res_str = {}
with open('test.json','rb') as f :
    res_json = loads(f.read())
# url = ''
# param = {}
# headers = {}
# re = requests.post(url,headers=headers,data=param)
#res_json = re.json()
try:
    date_array = res_json['data']['array']
except Exception as e:
    exit(e)
date_finallen = 30
date_len = len(date_array)
print(date_len)
date_end = date_finallen - date_len
array = date_array
if date_len < date_finallen:
    for i in range(date_end):
        array.append(array[0])
    res_json['data']['array'] = array
    json_res = dumps(res_json, ensure_ascii=False)
    print(json_res)
    clipboard.copy(json_res)
else:
	print("达到分页标准，不需要生成")


