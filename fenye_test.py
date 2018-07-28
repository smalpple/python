from json import *
import clipboard
res_json = {"message":"查询成功","status":"success","data":{"array":[{"fee":2,"downloadCount":47,"vipFee":1,"authorName":"孙庆新@微商水印相的","courseid":23,"vipFree":0,"courseSize":862,"courseType":2,"courseIcon":"https://resourcessl.edujia.com/ws/vip/courseware/icon/word_icon.png","introduction":"本次测试报告为UEM4.4的性能测试总结报告，目的在于总结性能测试工作，并分析测试结果，描述是否符合性能需求。预期参考人员包括用户、测试人员、开发人员、项目管理者、质量管理人员和需要阅读本报告的高层管理人员。","courseName":"性能测试报告性能测试报告性能测试报告性能测试报告"}]},"code":200}
date_array = res_json['data']['array']
date_finallen = 5
date_len = len(date_array)
if date_len <= date_finallen:
    date_end = date_finallen - date_len
    array = date_array
    for i in range(date_end):
        array.append(array[0])
    res_json['data']['array'] = array
    json_res = dumps(res_json, ensure_ascii=False)
    print(json_res)
    clipboard.copy(json_res)

else:
	print("达到分页标准，不需要生成")

