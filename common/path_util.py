#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os


class pathutil():

    def get_path_project(self):
        porject_path=os.path.dirname(os.path.dirname(__file__))
        return  porject_path








# if __name__ == '__main__':
#     a=pathutil().get_path_project()
#     print(a)