#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class getnestutil():



    def get_dic_nest(self, dic, objkey, default):
        """
        获取字典中的key对应的值，适用于字典嵌套
        dic:已知的字典
        objkey:已知的键--key
        default:找不到时返回的默认值
        """
        dic1 = dic
        for key, value in dic1.items():
            if key == objkey:
                return value

            else:
                if isinstance(value, dict):
                    new_value = getnestutil().get_dic_nest(value, objkey, default)
                    if new_value is not default:
                        return new_value
        return default
