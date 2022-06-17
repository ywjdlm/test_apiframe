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


    def get_dic_nest(self,dic, objkey, default=None):
        """
        获取字典中的key对应的值，适用于字典嵌套
        dic:已知的字典
        objkey:已知的键--key
        default:找不到时返回的默认值
        """
        try:
            dic1=dic
            for key,value in dic1.items():
                if key == objkey:
                    return value
                else:
                    if isinstance(value,dict):
                        new_value=Yamlutil().get_dic_nest(value,objkey,default)
                        if new_value is not default:
                            return new_value
            return default
        except:
            raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')


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

    def diguichaxun(self, yaml_file, objkey, ex_value, default=None, groupname=None):
        try:
            # if groupname is not None:
            #     data = Yamlutil().read_moreAPI_Yaml(yaml_file, groupname)
            # else:
            #     data = Yamlutil().read_moreAPI_Yaml(yaml_file)
            data = Yamlutil().read_moreAPI_Yaml(yaml_file, groupname)
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

if __name__ == '__main__':
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
      data = {"code": 0, "data": {
    "area": {"1": "东湖风景区", "10": "东西湖区", "11": "武汉经济技术开发区（汉南）", "12": "蔡甸区", "13": "江夏区", "14": "黄陂区", "15": "新洲区",
             "2": "东湖新技术开发区", "3": "江岸区", "4": "江汉区", "5": "硚口区", "6": "汉阳区", "7": "武昌区", "8": "青山区", "9": "洪山区"},
    "companytype": {"1": "全部", "2": "企业", "3": "个人组织", "4": "国家单位", "5": "事业单位"},
    "education": {"1": "全部", "2": "高中", "3": "大专", "4": "本科", "5": "研究生", "6": "博士及以上"},
    "maritalStatus": {"1": "未婚", "2": "已婚"},
    "userInfo": {"id": 129, "createdAt": "2022-05-31T14:17:53+08:00", "updatedAt": "2022-06-12T18:02:20+08:00",
                 "username": "", "openid": "", "nickname": "我爱我家我爱我家我",
                 "avatar": "static/uploads/20220601/4fd19ebcbb226282c258b2022e99faec.jpg", "age": 36, "gender": 1,
                 "height": 220, "danweiType": 5, "authDanwei": 2, "authReal": 2, "birthday": "1986/06/01",
                 "occupation": "烘焙师",
                 "photo": "static/uploads/20220601/8ab9659360e7c699adbd1d9720e7bb14.jpg,static/uploads/20220601/a29fa6354e3ee2835edb49945e077f76.jpg,static/uploads/20220601/395a2eed55611a9a34ca32a6f4bba54f.jpg,static/uploads/20220601/9c7bda0f34e37173e4e565082517b9e2.jpg",
                 "education": 5, "live": "唐山", "about": "大家好，我是来自海洋，家住珊瑚中，朋友大多是小虾，我很期待遇见我的另一个她，哈哈哈哈哈",
                 "desire": "期望遇见善良，稳重，传统的女孩子，这是我的理想型，小胖子，哈哈哈", "wxCode": "hahahah", "isLike": 0, "mutualLike": 0,
                 "isLooking": 0, "likeMinheight": 120, "likeMaxheight": 220, "likeMinAge": 18, "likeMaxage": 45,
                 "likeDanweiType": 1, "likeEducation": 1, "likeOccupation": "",
                 "photos": ["static/uploads/20220601/8ab9659360e7c699adbd1d9720e7bb14.jpg",
                            "static/uploads/20220601/a29fa6354e3ee2835edb49945e077f76.jpg",
                            "static/uploads/20220601/395a2eed55611a9a34ca32a6f4bba54f.jpg",
                            "static/uploads/20220601/9c7bda0f34e37173e4e565082517b9e2.jpg"], "tagList": [
            {"id": 246, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00", "uid": 129,
             "tagName": "运动"},
            {"id": 247, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-0 5-31T16:11:56+08:00", "uid": 129,
             "tagName": "服饰"},
            {"id": 248, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00", "uid": 129,
             "tagName": "打游戏"},
            {"id": 249, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00", "uid": 129,
             "tagName": "阅读"},
            {"id": 250, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00", "uid": 129,
             "tagName": "音乐"}], "educationExtend": "研究生", "area": 0, "maritalStatus": 1, "status": 1}}, "msg": "操作成功"}
      a = Yamlutil().get_dic_nest(data, 'wxCode')
      print(a)
      b=Yamlutil().diguichaxun('yongli.yml','data','15717823601',groupname='getcode')
      print(b)

