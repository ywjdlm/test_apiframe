#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

from common.log_util import logutil


class assertutil():

    def assert_code(self,code,except_code):
        """
        验证状态码
        :param code: 实际值
        :param except_code: 期望值
        :return:
        """
        try:
            assert code==except_code
            return True

        except:
            #logutil().error(" 实际结果:  code=%s , except_code=%s , 断言失败!" %(code,except_code))
            return False
            # raise

    def assert_body(self,body,body_msg,except_body_msg):
        """
        验证body的任意字段的值
        :param body:响应体
        :param body_msg:实际结果的字段
        :param except_body_msg:预期结果
        :return:
        """
        try:
            msg=body[body_msg]
            assert msg==except_body_msg
            return True

        except:
            #logutil().error(" 实际结果:  body_msg=%s , except_body_msg=%s , 断言失败!" %(msg,except_body_msg))
            return False
            # raise

    def assert_in_body_msg(self,body,except_data):
        """
            验证response body中是否包含预期字符串
            :param body:
            :param expected_msg:
            :return:
            """
        try:
            #  把字典的格式转化为str格式
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert except_data in text
            return True

        except:
            #logutil().error("Response body Does not contain expected_msg , expected_msg = %s , Response_body = %s , 断言失败!" % (except_data,body))
            return False
            # raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            #logutil().error("Response body != expected_msg , expected_msg = %s , body = %s , 断言失败!" % (expected_msg, body))
            return False
            # raise

    def assert_time(self, Response_time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert Response_time < expected_time
            return True

        except:
            #logutil().error("Response time > expected_time , expected_time is %s , Response_time is %s , 断言失败!" % (expected_time, Response_time))
            return False
            # raise


# if __name__ == '__main__':
    # 断言状态码
    # code=404
    # ex_code=200
    # assertutil().assert_code(code,ex_code)

    # 断言响应体信息
    # r={"code":"200",
    #    "msg":"操作成功",
    #     "data":{
    #     "content": "哦哦哦哦",
    #     "type": "5",
    #     "labelId": "49"
    #            }
    #     }
    #
    #
    # ex_msg={
    #     "content": "哦哦哦哦",
    #     "type": "6",
    #     "labelId": "49"
    # }

    # data={"content": "哦哦哦哦","type": "6","labelId": "48"}
    # ex_msg = {"labelId": "49"}
    #
    # assertutil().assert_body(data,'labelId',ex_msg)

    #断言响应体包含预期字符串
    # data = {"content": "哦哦哦哦", "type": "6", "labelId": "48","msg":"操作成功"}
    # ex_str="成功1"
    # assertutil().assert_in_body_msg(data,ex_str)

    #断言字符串相等
    # assertutil().assert_text("成功!","成功")

    #断言响应时间
    #assertutil().assert_time(35,30)
