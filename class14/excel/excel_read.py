'''
@author:lvming
@time:2021/7/2
'''
from class13.class13_xuzhu.api_keyword.api_key import ApiKey
import openpyxl


# excel测试用例的读取与执行
excel = openpyxl.load_workbook('api_cases.xlsx')
sheet = excel['Sheet1']
ak = ApiKey()
for value in sheet.values:
    # print(value)
    # 准备数据—模拟请求——校验结果
    if type(value[0]) is int:
        # 准备测试对象
        url = value[1]+value[2]
        headers = value[4]
        data = value[5]
        data_type = value[6]
        assert_value = value[7]
        expect_value = value[8]
        if value[4]:
            if value[5]:
                dict_data = {
                    'url':url,
                    'headers': eval(value[4]),
                    # 'data':data
                    data_type:eval(data)
                }
            else:
                dict_data = {
                    'url': url
                }
        print(dict_data)
        # list = [url,headers,data,data_type]
        # print(list)
        # 模拟请求
        # res = getattr(ak,value[3])(url=url,headers=headers,json=data)
        res = getattr(ak,value[3])(**dict_data)
        # # 校验结果
        result=ak.get_text(res.text,assert_value)
        # assert result == value[8],'预期与实际不符合'
        # print(result+"-------------"+expect_value)
        print(ak.assert_text(result,expect_value))

