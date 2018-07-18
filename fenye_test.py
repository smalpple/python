from json import *
res_json = {
	"code": 200,
	"status": "success",
	"message": "操作成功",
	"data": {
		"array": [{
			"createTime": "2018-06-26 14:33:18",
			"recashName": "升级合伙人奖励（一级）",
			"recashFee": 3,
			"inviteeName": "148****8884"
		}, {
			"createTime": "2018-06-26 14:31:51",
			"recashName": "升级合伙人奖励（一级）",
			"recashFee": 3,
			"inviteeName": "148****8884"
		}, {
			"createTime": "2018-06-26 14:29:37",
			"recashName": "升级合伙人奖励（一级）",
			"recashFee": 3,
			"inviteeName": "148****8884"
		}, {
			"createTime": "2018-06-26 14:29:09",
			"recashName": "升级合伙人奖励（一级）",
			"recashFee": 3,
			"inviteeName": "148****8884"
		}, {
			"createTime": "2018-06-26 14:26:53",
			"recashName": "升级合伙人奖励（一级）",
			"recashFee": 3,
			"inviteeName": "148****8884"
		}]
	}
}
date_array = res_json['data']['array']
date_finallen = 30
date_len = len(date_array)
if date_len <= date_finallen:
    date_end = date_finallen - date_len
    array = date_array
    for i in range(date_end):
        array.append(array[0])
    res_json['data']['array'] = array
    json_res = dumps(res_json, ensure_ascii=False)
    print(json_res)
else:
	print("达到分页标准，不需要生成")

