#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

import pytest
#所有的用例一起运行,主运行写在此代码文件中,即开关
from common.path_util import pathutil
from common.sendmail_util import sendmailutil
from config.ini_util import iniutil

if __name__ == '__main__':
    pytest.main()
    print('测试GIT111')
    print('test,success')
    print('可能会pull失败？')
    print('选择第一个')
    print('pull接成功了?')
    #hahahha