#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging
import os
import time
from logging.handlers import RotatingFileHandler

from common.path_util import pathutil


def get_current_time():
    return time.strftime(logutil().current_time, time.localtime(time.time()))


class logutil():


    # 获取logger对象,取名log
    logger = logging.getLogger("log")
    logger.setLevel(logging.DEBUG)
    # 创建文件目录
    logs_dir = pathutil().get_path_project() + "\\logs"
    if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        pass
    else:
        os.mkdir(logs_dir)
    # 创建日志文件
    timestamp = time.strftime("%Y%m%d", time.localtime())
    logfilename = '%sProjectlog.txt' % timestamp
    logfilepath = os.path.join(logs_dir, logfilename)
    #获取文件日志句柄,filename文件名,maxBytes 允许日志文件最大为100MB,backupCount最多备份10个文件
    rotatingFileHandler = RotatingFileHandler(filename=logfilepath, maxBytes=1024 * 1024 * 100, backupCount=10)
    current_time='%Y-%m-%d %H:%M:%S'

    #设置控制器显示日志信息
    # console = logging.StreamHandler()
    # console.setLevel(logging.NOTSET)
    # logger.addHandler(console)

    @staticmethod
    def debug(log_msg):
        #添加句柄
        logutil().logger.addHandler(logutil().rotatingFileHandler)
        #设置输出格式
        logutil().logger.debug("[DEBUG " + get_current_time() + "]" + log_msg)
        #移除句柄
        logutil().logger.removeHandler(logutil().rotatingFileHandler)

    @staticmethod
    def info(log_msg):
        #添加句柄
        logutil().logger.addHandler(logutil().rotatingFileHandler)
        #设置输出格式
        logutil().logger.info("[INFO " + get_current_time() + "]" + log_msg)
        #移除句柄
        logutil().logger.removeHandler(logutil().rotatingFileHandler)

    @staticmethod
    def warning(log_msg):
        #添加句柄
        logutil().logger.addHandler(logutil().rotatingFileHandler)
        #设置输出格式
        logutil().logger.warning("[WARNING " + get_current_time() + "]" + log_msg)
        #移除句柄
        logutil().logger.removeHandler(logutil().rotatingFileHandler)

    @staticmethod
    def error(log_msg):
        #添加句柄
        logutil().logger.addHandler(logutil().rotatingFileHandler)
        #设置输出格式
        logutil().logger.error("[ERROR " + get_current_time() + "]" + log_msg)
        #移除句柄
        logutil().logger.removeHandler(logutil().rotatingFileHandler)

    @staticmethod
    def critical(log_msg):
        #添加句柄
        logutil().logger.addHandler(logutil().rotatingFileHandler)
        #设置输出格式
        logutil().logger.critical("[CRITICAL " + get_current_time() + "]" + log_msg)
        #移除句柄
        logutil().logger.removeHandler(logutil().rotatingFileHandler)


# if __name__ == '__main__':
#     logutil().debug("我是一个debug的日志,啦啦啦")
#     logutil().info("我是info日志信息,哈哈哈")
#     logutil().warning("这是一个warning级别的日志")
#     logutil().error("这是一个erro级别的日志信息")
#     logutil().critical("我是一个critical非常严重级别的日志信息,要注意噢!!!")
#     logutil.info('我没有括号,这就是@staticmethod的其中一个用法')






