#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

logs_dir = os.path.abspath('..') + "\logs"
logfilename='日志'
logpath=os.path.join(logs_dir, logfilename)
print(logpath)