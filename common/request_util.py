#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
from logging import exception

import requests


class requestsutil:
    # session = requests.session()


    def send_request(self,method, url, headers, data,**kwargs):
        method = str(method).lower()  # 将method的值强制转换成小写
        if method == 'get':
            data=json.loads(data)
            res = requests.request(method,url=url,params=data,**kwargs)
            return res.text

        elif method == 'post':
            data=json.loads(data)
            res = requests.request(method,url=url,data=data,**kwargs)
            return res.text