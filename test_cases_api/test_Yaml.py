#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import pytest

from case_data.Yaml_util import Yamlutil


# case=excelutil().read_excel(os.getcwd()+'\case_data\Cases.xlsx','1.登录')
# print(case)

#yaml文件中一组接口数据为一个用例
from common.assert_util import assertutil
from common.exce_lutil import excelutil
from common.log_util import logutil
from config.ini_util import iniutil


class Testceshi:

    @pytest.mark.parametrize('caseinfo',Yamlutil().read_moreAPI_Yaml('casesYaml.yaml'))
    def test01(self,caseinfo,connect_mysql):
        print(caseinfo)
        print(caseinfo['name'])
        print(caseinfo['request'])
        print(caseinfo['Assert'])
        data=json.dumps(caseinfo['request'])
        logutil().info('   name :'+caseinfo['name']+"  ,  "+"reponse :"+data)

    def test02(self,clear_extract):
        print("测试用例2")
        Yamlutil().write_extract_yaml({"name": "张三"})
        Yamlutil().write_extract_yaml({"name1": "李四"})

    def test03(self):
        # 读取yaml文件参数值
        res_name=Yamlutil().read_extract_yaml('name')
        print(res_name)

    @pytest.mark.parametrize('caseinfo',Yamlutil().read_moreAPI_Yaml('rl_api.yaml'))
    def test04(self,caseinfo):
        # 组合url访问
        # print(caseinfo)
        url=iniutil().get_confini('test','url')+caseinfo['request']['url']
        a=assertutil().assert_code(200,caseinfo['assert']['code'])
        #判断用例是否断言成功
        if a==True:
            logutil().info("   这里是接口的返回值:  " + url+",  断言成功!!!")
        else:
            logutil().error("  用例断言失败,  请求情况:xxxxxxxxxxxx ,  这里是接口的返回值:  " + url + "  ,  实际结果:  " + "200(这里可以通过返回的实际值取)")

    @pytest.mark.parametrize('cs',Yamlutil().read_moreAPI_Yaml('rl_api.yaml'))
    def test05(self,cs):
        #判断多个断言
        a = assertutil().assert_code(200, cs['assert']['code'])
        b =assertutil().assert_in_body_msg('恭喜你,操作成功',cs['assert']['data'])
        print(b)
        if a==True and b==True:
            logutil().info("  这里是接口的返回值:  " + str(a)+",  断言成功!!!")
        else:
            logutil().error("  用例断言失败,  请求情况:xxxxxxxxxxxx ,  这里是接口的返回值:  " + str(a) + "  ,  实际结果:  " + "200(这里可以通过返回的实际值取)"+"另外一个实际结果:  "+ str(b))


    @pytest.mark.parametrize('baogao',Yamlutil().read_moreAPI_Yaml('rl_api.yaml'))
    def test06(self,baogao,first_write):
        #生成excel格式的报告
        req="实际结果xxxxx"
        a=assertutil().assert_code(200, baogao['assert']['code'])
        if a==True:
            b='pass'
        else:
            b='fail'
        excel_data=[baogao['name'],baogao['request']['method'],json.dumps(baogao['request']['params']),
                    req,b]
        excelutil().write_data(excel_data)
        # print(json.dumps(baogao['request']['params']),type(json.dumps(baogao['request']['params'])))

    @pytest.mark.parametrize('yongli', Yamlutil().read_moreAPI_Yaml('yongli.yml',groupname='gettoken'))
    def test07(self,yongli):
        print(yongli)


if __name__ == '__main__':
    pytest.main(['test_Yaml.py'])




