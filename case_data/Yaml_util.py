#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#主要用于读取yaml文件

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from logging import exception
from string import Template

import requests
import yaml

from common.path_util import pathutil


class Yamlutil():


    # def read_casesYaml(self,yaml_file):
    #     """读取yaml用例"""
    #     with open(pathutil().get_path_project()+"\\case_data\\cases\\"+yaml_file, mode='r', encoding='utf-8') as f:
    #         value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
    #         # print(value)
    #         return value;

    def read_moreAPI_Yaml(self,yaml_file,groupname=None):
        """
        读取一个yaml文件中放多个接口的用例的方法或者单个接口的方法
        """
        if groupname is not None:
            with open(pathutil().get_path_project()+"\\case_data\\cases\\"+yaml_file, mode='r', encoding='utf-8') as f:
                caseinfo=yaml.load(stream=f.read(),Loader=yaml.FullLoader)
                case_API=caseinfo[groupname]
                return case_API
        else:
            with open(pathutil().get_path_project() + "\\case_data\\cases\\" + yaml_file, mode='r',
                      encoding='utf-8') as f:
                value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
                # print(value)
                return value

    """
    extract临时文件读写清空操作
    1.key为键值对格式或者键=值格式传参
    """
    # 读取extract.yaml
    def read_extract_yaml(self,key):
        with open(pathutil().get_path_project()+"\\case_data\\extract.yaml", mode="r", encoding="utf-8") as f:
            value =yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key];


    #写入yaml文件,写到extract.yaml中,yaml/yml都是yaml文件后缀
    def write_extract_yaml(self,data):
        with open(pathutil().get_path_project()+"\\case_data\\extract.yaml", mode="a", encoding="utf-8") as f:# mode="a",w覆盖写入,a是追加
            value = yaml.dump(data=data,stream=f, allow_unicode=True)
            return value;

    #清除yaml文件的内容
    def clear_extract_yaml(self):
        with open(pathutil().get_path_project()+"\\case_data\\extract.yaml", mode="w", encoding="utf-8") as f:
            f.truncate()




    # 利用Template方法,替换yaml文件的变量
    def Yaml_replace(self, yaml_file, groupname, dic):
        """
        Template 中主要的俩种格式：
        1：$variable 使用 $变量名 引用变量
        2：${variable} 使用 ${变量名} 大括号包起来,在yaml文件里定义变量: ${变量名}
        eg:创建yaml文件，将数据存放进去，当中设置 username 为${user} ，password为 $password

        """
        # 打开yaml文件并读取
        with open(os.getcwd() + "\\case_data\\cases\\"+yaml_file, mode='r', encoding='utf-8') as f:
            read_res = f.read()
            # 获取yaml文件中的对应格式变量
            temp = Template(read_res)
            try:
                # 将写入的数据传输到变量中,获取新的值
                c = temp.safe_substitute(dic)
                yaml_data = yaml.safe_load(c)
                case_API = yaml_data[groupname]
                return case_API
            except:
                raise FileNotFoundError("需要替换的数据格式不为字典格式!!!")




