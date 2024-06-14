#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from case_data.Yaml_util import Yamlutil
from common.getnest_util import getnestutil


class nestselectutil():

    # 嵌套字典分解后对比
    def get_dic_nest(self, dic, objkey=None, default=None, values=None):
        """
            获取字典中的key对应的值，适用于字典嵌套
            dic:已知的字典
            objkey:已知的键--key
            default:找不到时返回的默认值
        """
        # 此分支使用键进行模糊查询
        if values is None and objkey is not None:
            try:
                # 获取所有的键
                for key in dic.keys():
                    if key == objkey:
                        return key
                    else:
                        if isinstance(dic[key], dict):
                            new_key = nestselectutil().get_dic_nest(dic[key], objkey=objkey, default=default, values=values) # 循环判断
                            if new_key is not default:
                                return new_key
                return default
            except:
                raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')

        # 此分支表示已知值,但不知道键时,进行模糊查询
        elif objkey == None and values is not None:
            try:
                for k, v in dic.items():
                    if v == values:
                        return v
                    else:
                        if isinstance(v, dict):
                            new_v = nestselectutil().get_dic_nest(v,values=values)  # 循环判断
                            if new_v is not default:
                                return new_v
                return default
            except:
                raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')

        # 此分支表示值和键都知道,去精确查询某一个字典信息
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
                        if value == values:
                            return value
                    else:
                        # 判断值是否为字典,如果为字典则再判断一次,直到得到相同的键的值为止
                        if isinstance(value, dict):
                            new_value = nestselectutil().get_dic_nest(value, objkey=objkey,values=values, default=default)
                            # 如果找到值就返回新值,没找到就返回默认
                            if new_value is not default:
                                return new_value
                return default
            except:
                raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')

    def diguichaxun(self, lis_data=None,yaml_files=None, key=None, ex_value=None, default=None, groupnames=None):
        """
        :param lis_data: 字典格式的列表
        :param yaml_files: yml文件
        :param key: 已知键
        :param ex_value: 已知值
        :param default: 默认值
        :param groupnames: yml文件中的组名
        :return: 最终返回查询到的结果,精确查询就是一个字典格式,模糊查询则为一个列表
        """
        # 判断是否传入yml文件
        if yaml_files is not None:
            try:
                # 获取yaml文件的值,即列表
                data = Yamlutil().read_moreAPI_Yaml(yaml_file=yaml_files, groupname=groupnames)
            except:
                raise FileNotFoundError('输入的yaml文件格式错误!!!')
        else:
            data=lis_data


        # 此分支用于使用键进行模糊查询,ex_value用于分支走向的判断,key已知键
        if ex_value == None:
            lis = []
            try:
                # read_moreAPI_Yaml返回的是一个列表格式
                # 先将列表拆成一个个字典
                for i in data:
                    a = nestselectutil().get_dic_nest(i,objkey=key) # 已知字典和键,如果查到字典里面有这个键,则返回此字典中的 键
                    if key == a:
                        lis.append(i)
                return lis # 最终会返回一个列表
            except:
                return default

        #此分支用于通过值模糊查询字典
        elif key==None:
            li=[]
            try:
                for i in data:
                    a = nestselectutil().get_dic_nest(i, values=ex_value)
                    if isinstance(str(a), str):
                        if a == ex_value:
                            li.append(i)
                return li
            except:
                return default



        # 此分支用于精确查询,ex_value不能为空,判断查询到的键值是否是我想要的
        else:
            # read_get_test_yml返回的是一个列表格式
            # 先将列表拆成一个个字典
            if ex_value is not None:
                for i in data:
                    try:
                        # 如果ex_value有值,则走向get_dic_nest里的else方法,判断值的类型,
                        # 从而对比返回的值是否正确,若正确则返回一条精准数据,适用于精准查询,有且只有一条数据
                        a = nestselectutil().get_dic_nest(i, objkey=key,values=ex_value,default=default)
                        if isinstance(a, str):
                            if ex_value == a:
                                return i
                        elif isinstance(a, int):
                            if ex_value == a:
                                return i
                        else:
                            if a == None:
                                pass
                            else:
                                if ex_value in a.values():
                                    return i
                    except:
                        return default
            else:
                return default

    # 获取嵌套字典的已知键 所对应的 值,最终返回已知键的值,可能存在返回的值不是唯一的情况,嵌套中可能存在相同的键,此时查询就会导致无法获取所有的值
    def get_dic_nest_val(self, dic, objkeys, default=None):
        """
        获取字典中的key对应的值，适用于字典嵌套
        dic:已知的字典
        key:已知的键--key
        default:找不到时返回的默认值
        """
        try:
            dic1 = dic
            for key, value in dic1.items():  # 遍历字典的键和值
                if key == objkeys:  # 对比获取的键和已知的键,如果相等则返回键对应的值
                    return value
                else:       # 如果不相等则查看值是否是字典,再分解值,进行循环判断
                    if isinstance(value, dict):
                        new_value = getnestutil().get_dic_nest(value, objkeys, default)
                        if new_value is not default:
                            return new_value  # 最终返回根据已知键查询到的值
            return default  # 如果没找到,返回默认值
        except:
            raise FileNotFoundError('数据格式有误,无法执行,请检查数据格式!!!')


if __name__ == '__main__':
    # 测试精确查询,已知key和值的时候
    a = nestselectutil().diguichaxun(yaml_files='yongli.yml', key='x-token',ex_value=123,groupnames='login')
    print(a)

    # 测试已知值ex_value,查用例
    A = nestselectutil().diguichaxun(yaml_files='yongli.yml', ex_value='失败',groupnames='login')
    print(A)

    #测试已知键key查用例
    B = nestselectutil().diguichaxun(yaml_files='yongli.yml', key='mobile',groupnames='getcode')
    print(B)

    print(nestselectutil().diguichaxun())

    # 测试get_dic_nest_val和diguichaxun的else分支data=lis_data的走向,
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
                {"id": 246, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00",
                 "uid": 129,
                 "tagName": "运动"},
                {"id": 247, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-0 5-31T16:11:56+08:00",
                 "uid": 129,
                 "tagName": "服饰"},
                {"id": 248, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00",
                 "uid": 129,
                 "tagName": "打游戏"},
                {"id": 249, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00",
                 "uid": 129,
                 "tagName": "阅读"},
                {"id": 250, "createdAt": "2022-05-31T16:11:56+08:00", "updatedAt": "2022-05-31T16:11:56+08:00",
                 "uid": 129,
                 "tagName": "音乐"}], "educationExtend": "研究生", "area": 0, "maritalStatus": 1, "status": 1}},
            "msg": "操作成功"}
    b=nestselectutil().get_dic_nest_val(data,objkeys='tagList')
    print(b)
    c=nestselectutil().diguichaxun(lis_data=b,key='id')
    print(c)

