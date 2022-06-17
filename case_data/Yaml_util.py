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



    #此方法查询嵌套字典的方法
    def get_dic_nest(self,dic, objkey, default=None,values=None):
        #此分支用于多个嵌套字典模糊查询
        if values is not None:
            try:
                for key in dic.keys():
                    if key == objkey:
                        return key
                    else:
                        if isinstance(dic[key], dict):
                            new_key = Yamlutil().get_dic_nest(dic[key], objkey, default,values=values)
                            if new_key is not default:
                                return new_key
                return default
            except:
                raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')
        else:
            """
                   获取字典中的key对应的值，适用于字典嵌套
                   dic:已知的字典
                   objkey:已知的键--key
                   default:找不到时返回的默认值
                   """
            try:
                dic1 = dic
                # 获取字典的键和值,判断字典的键是否等于已知的键
                for key, value in dic1.items():
                    if key == objkey:
                        return value
                    else:
                        # 判断值是否为字典,如果为字典则再判断一次,直到得到相同的键的值为止
                        if isinstance(value, dict):
                            new_value = Yamlutil().get_dic_nest(value, objkey, default)
                            # 如果找到值就返回新值,没找到就返回默认
                            if new_value is not default:
                                return new_value
                return default
            except:
                raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')



    def diguichaxun(self, yaml_file, objkey, ex_value=None, default=None, groupname=None,val=None):
        try:
            data = Yamlutil().read_moreAPI_Yaml(yaml_file, groupname)
        except:
            raise FileNotFoundError('输入的yaml文件格式错误!!!')

        # 此分支用于多个嵌套字典模糊查询,配合get_dic_nest中当values不为None的时候执行
        if val is not None:
            lis = []
            try:
                # read_get_test_yml返回的是一个列表格式
                # 先将列表拆成一个个字典
                for i in data:
                    a = Yamlutil().get_dic_nest(i, objkey, values=val)
                    if objkey == a:
                        lis.append(i)
                return lis
            except:
                raise Exception("数据格式解析失败,请检查传入参数格式!!!!")

         #此分支用于精确查询,尤其是针对单个嵌套字典时,若传入的键和值在yml文件中有多个,建议使用模糊查询
        else:
            # read_get_test_yml返回的是一个列表格式
            # 先将列表拆成一个个字典
            if ex_value is not None:
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
            else:
                raise Exception('方法中ex_value未填写,无法判断!!!')


    #通过键值对来判断返回值
    def mohu_nest(self,dic, objkey, value,default=None):
        try:
            for k,v in dic.keys():
                if k == objkey:
                    if dic[k]==value:
                        return v
                else:
                    if isinstance(v, dict):
                        new_v = Yamlutil().mohu_nest(v, objkey,value)
                        if new_v is not default:
                            return new_v
            return default
        except:
            raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')

    #通过键值对模糊查询所有的字典数据,返回一个列表结果
    def mohuselect_dic(self,yaml_file, objkey, ex_value, default=None, groupname=None):
        try:
            data = Yamlutil().read_moreAPI_Yaml(yaml_file, groupname)
        except:
            raise FileNotFoundError('输入的yaml文件格式错误!!!')
        try:
            li=[]
            for i in data:
                    a = Yamlutil().get_dic_nest(i, objkey, default)
                    if isinstance(str(a), str):
                        if a == ex_value:
                                li.append(i)
            return li
        except:
            Exception('没有找到匹配的数剧,请查阅对应yaml文件!!!')



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

        # 利用Template方法,
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

if __name__ == '__main__':

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
      # a = Yamlutil().get_dic_nest(data, 'wxCode')
      # print(a)
      # b=Yamlutil().diguichaxun('yongli.yml','assert','成功',groupname='login')
      # print(b)
      #
      # c=Yamlutil().diguichaxun('yongli.yml','heads',val='1',groupname='login')
      # print(c)

      d=Yamlutil().mohuselect_dic('yongli.yml','assert',ex_value='失败',groupname='login')
      print(d)
