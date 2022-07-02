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







if __name__ == '__main__':
    a=pathutil().get_general_path()
    print(a)



