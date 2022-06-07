#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
    需要执行用例之前/之后所需的操作写在此文件即可
    @allure.epic("项目名称:app")#项目名称
    @allure.feature("请求时间")#功能/需求点/模块描述
    @allure.story("请求时间")#测试标题
    @allure.description("我是此用例的描述")#描述用例
    @allure.link(url="www.baidu.com",name="这是需求文档")#定义一个链接，在测试报告中展示
    @allure.issue(url="www.baidu.com",name="需求来自如邻生活圈")#关联缺陷系统内的缺陷链接
    @allure.severity("critical")#定义用例严重级别
    @allure.attach() #测试报告内添加附件
    @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址
    allure.environment(environment=env) #用于定义environment
    @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
"""
import time

import pytest

# 连接数据库
from case_data.Yaml_util import Yamlutil
from common.database_util import databaseutil
from common.exce_lutil import excelutil

#连接数据库
from common.sendmail_util import sendmailutil


@pytest.fixture(autouse=False)
def connect_mysql():
    con=databaseutil().db
    print("数据库连接成功")
    yield
    con.close()
    print("数据库断开成功")

#运行前清除extract.yaml里的数据
@pytest.fixture()
def clear_extract():
    Yamlutil().clear_extract_yaml()
    print('yaml文件清除成功')


#写入测试execl类型的测试报告,并执行完用例写入测试报告后发送邮件
@pytest.fixture(scope='module',autouse=False)
def first_write():
    excelutil().create_Yaml_excel()
    print('用例执行前自动创建一个空表')
    yield
    file=excelutil().savepath
    sendmailutil().send_mail("1571754405@qq.com",file)
    sendmailutil().send_mail("980975647@qq.com", file)
    print("用例执行结束,邮件发送成功")






