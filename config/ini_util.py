#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import configparser
import os

from common.log_util import logutil
from common.path_util import pathutil


class iniutil:
    conf = configparser.ConfigParser()  # 实例化一个ini文件的操作对象

    # 读取配置文件
    def read_confini(self):
        filepath = pathutil().get_path_project() + '\\config\\conf.ini'
        # 判断配置文件是否存在,若不存在抛出提示
        if not os.path.exists(filepath):
            raise FileNotFoundError("文件不存在")
        iniutil().conf.read(filepath, encoding='utf-8')  # 读取ini配置文件

    # 获取配置文件的具体值
    def get_confini(self, Section, value):
        iniutil().read_confini()
        """
             配置文件读取
             :param title:
             :param value:
             :return:
             """
        return self.conf.get(Section, value)

    # 写入配置文件
    def write_confini(self, Sections, key, value):
        try:
            iniutil().read_confini()
            list = []
            list = iniutil().conf.sections()  # 获取到配置文件中所有分组名称
            if Sections not in list:  # 如果分组Sections不存在则插入Sections分组
                iniutil().conf.add_section(Sections)
                iniutil().conf.set(Sections, key, value)  # 给type分组设置值
                # conf.set(Sections, 'mail', '123456@qq.com')
                o = open(pathutil().get_path_project() + '\\config\\conf.ini', 'w')
                iniutil().conf.write(o)
                o.close()  # 不要忘记关闭
            else:
                print("此" + Sections + "值可能已存在,请检查!")
        except:
            print("配置文件可能存在异常,请检查配置文件数据!")

    # 删除conf.ini文件某个组
    def del_confini_allSections(self, Sections):
        iniutil().read_confini()
        list1 = []
        list1 = iniutil().conf.sections()
        if Sections in list1:
            iniutil().conf.remove_section(Sections)  # 删除配置文件中type分组
            o = open(pathutil().get_path_project() + '\\config\\conf.ini', 'w')
            iniutil().conf.write(o)
            o.close()  # 不要忘记关闭
            print(Sections + "删除成功")
        else:
            print("此" + Sections + "不存在")

    # 删除conf.ini文件某个组里面的值
    def del_confini_keys(self, Sections, key):
        iniutil().read_confini()
        list2 = []
        list2 = iniutil().conf.sections()
        if Sections in list2:
            try:
                iniutil().conf.remove_option(Sections, key)  # 删除Sections分组的键值对
                o = open(pathutil().get_path_project() + '\\config\\conf.ini', 'w')
                iniutil().conf.write(o)
                o.close()  # 不要忘记关闭
                print(Sections + "下的" + key + "删除成功")
            except:
                print("操作失败,请查看配置文件是否存在该key")
        else:
            print("此" + Sections + "不存在,删除失败")

if __name__ == '__main__':

    # # iniutil().del_confini_allSections('mm')
    # sendaddr = iniutil().conf.get('mail', 'sendaddr')
    # QQ_pwd = iniutil().conf.get('mail', 'QQ_pwd')
    # print(os.path.abspath('..') + '\config\conf.ini')
    # print(os.getcwd())
    # host_dev = iniutil().get_confini('mysql-dev', 'host')
    # print(host_dev)
    try:
        host=iniutil().get_confini('mysql-test', 'host')
        print(host)
    except:
        logutil().info("  "+pathutil().get_path_project() + '\\config\\conf.ini'+':    请检查配置文件!!!')