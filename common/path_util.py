#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys


class pathutil():

    # 此路径真能用于win系统
    def get_path_project(self):
        porject_path=os.path.dirname(os.path.dirname(__file__))
        return  porject_path


    # 此方法可用于win和linux系统,获取项目的路径
    def get_general_path(self):
        """
        __file__: 当前调用的py文件的位置
        os.path.abspath: 返回绝对路径,从根目录开始
        os.path.dirname(path): 返回path的上级目录
        :return: 返回项目绝对路径
        """
        general_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return general_path

    # 返回配置文件的绝对路径
    def get_config_path(self):
        config_dir=os.path.join(pathutil().get_general_path(),'config')
        config_path=os.path.join(config_dir,'conf.ini')
        return config_path

    # 返回extract.yaml文件绝对路径
    def get_casedata_path(self):
        casedata_dir=os.path.join(pathutil().get_general_path(),'case_data')
        return casedata_dir

    # 返回测试数据的绝对路径'
    def get_cases_path(self):
        case_path=os.path.join(pathutil().get_casedata_path(),'cases')
        return case_path

    # 返回logs日志目录的路径
    def get_log_path(self):
        logs_dir=os.path.join(pathutil().get_general_path(),'logs')
        # 如果目录存在,则跳过,不存在创建一个logs目录
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        return logs_dir

    # 返回excel报告的路径
    def get_excelreport_path(self):
        report_path = os.path.join(pathutil().get_general_path(), 'excel_report')
        return report_path



if __name__ == '__main__':
    a=pathutil().get_log_path()
    print(a)



