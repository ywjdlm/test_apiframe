#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pytest

from common.exce_lutil import excelutil
from common.log_util import logutil
from common.path_util import pathutil
from common.request_util import requestsutil

#根据excel表格执行用例方法
from common.sendmail_util import sendmailutil


class TestExcel:

    def test_01(self):
        cases = excelutil().read_excel(pathutil().get_path_project()+'\\case_data\\cases\\Cases.xlsx', '1.登录')

        excel_list=[]

        #读取指定excel文件的用例
        for unit_case in cases:
            case_id = unit_case.get("id")
            case_url = unit_case.get("url")
            case_name = unit_case.get("name")
            case_method = unit_case.get("method")
            case_headers = (unit_case.get("headers"))
            case_data = (unit_case.get("params"))
            req=requestsutil().send_request(method=case_method,url=case_url,headers=case_headers,data=case_data)
            print(req)
            if "成功" in req:
                a="pass"
            else:
                a="fail"

            #获取'用例名称','请求方法','请求参数','实际结果','断言结果'
            list=[case_name,case_method,case_data,req,a]
            excel_list.append(list)

            logutil().info('name :'+case_name+'  ,  '+'reponse :'+req)

        #创建测试报告
        excelutil().creat_excel('12report.xlsx')

        #查看测试报告
        # a=excelutil().load_exceldata(pathutil().get_path_project()+'\\excel_report\\report.xlsx','test_report')
        # print(a)





if __name__ == '__main__':
    pytest.main(['1_test_Excel.py'])
#     sendmailutil().send_mail('980975647@qq.com',pathutil().get_path_project()+'\\excel_report\\report.xlsx')
#     sendmailutil().send_mail('1571754405@qq.com',pathutil().get_path_project()+'\\excel_report\\report.xlsx')

