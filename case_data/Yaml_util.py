#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#主要用于读取yaml文件

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from logging import exception

import requests
import yaml

from common.path_util import pathutil


class Yamlutil():


    def read_casesYaml(self,yaml_file):
        """读取yaml用例"""
        with open(pathutil().get_path_project()+"\\case_data\\cases\\"+yaml_file, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            # print(value)
            return value;

    def read_moreAPI_Yaml(self,yaml_file,groupname):
        """
        读取一个yaml文件中放多个接口的用例的方法
        """
        with open(pathutil().get_path_project()+"\\case_data\\cases\\"+yaml_file, mode='r', encoding='utf-8') as f:
            caseinfo=yaml.load(stream=f.read(),Loader=yaml.FullLoader)
            case_API=caseinfo[groupname]
            return case_API;

    def diguichaxun(self, yaml_file, objkey, ex_value, default, groupname=None):
        try:
            if groupname is not None:
                data = Yamlutil().read_moreAPI_Yaml(yaml_file, groupname)
            else:
                data = Yamlutil().read_casesYaml(yaml_file)
        except:
            raise FileNotFoundError('输入的yaml文件格式错误!!!')
        # read_get_test_yml返回的是一个列表格式
        # 先将列表拆成一个个字典
        for i in data:
            try:
                a = Yamlutil().get_dic_nest(i, objkey, default)
                if isinstance(a, str):
                    if ex_value == a:
                        return i
                elif isinstance(a, int):
                    if ex_value == a:
                        return i
                else:
                    if ex_value in a.values():
                        return i
            except:
                raise FileNotFoundError('没有找到匹配的数剧,请查阅对应yaml文件!!!')

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

# if __name__ == '__main__':
#     print(Yamlutil().read_casesYaml('casesYaml.yaml'))
#     print(Yamlutil().read_casesYaml('cs.yaml'))
#     header = {"Content-Type": "application/x-www-form-urlencoded"}  # 请求头的参数
#
#     body = {"username": "15717823601", "password": "rl123456"}
#
#     r = requests.post(url="https://service.rulin.pro/auth/token", data=body, headers=header)  # 发送请求
#     Yamlutil().clear_extract_yaml()
#     Yamlutil().write_extract_yaml({"我丢":"我去"})
#     Yamlutil().write_extract_yaml({'token':r.json()["data"]["token"]})
#     a=Yamlutil().read_extract_yaml("我丢")
#     print(Yamlutil().read_extract_yaml("token"))
#     print(a)
