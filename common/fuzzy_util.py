#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re


class fuzzyutil():

    #用于数据模糊查询
    def fuzzy_finder(self,value, key, data):
        """
        模糊查找器
        :param key: 关键字
        :param data: 数据
        :return: list
        """
        # 结果列表
        suggestions = []
        # 非贪婪匹配，转换 'djm' 为 'd.*?j.*?m'
        # pattern = '.*?'.join(key)
        pattern = '.*%s.*' % (value)
        # print("pattern",pattern)
        # 编译正则表达式
        regex = re.compile(pattern)
        for item in data:
            # print("item",item['name'])
            # 检查当前项是否与regex匹配。
            match = regex.search(item[key])
            if match:
                # 如果匹配，就添加到列表中
                suggestions.append(item)

        return suggestions


# if __name__ == '__main__':
#     file_list = [
#         {
#             "type": "dir",
#             "size": "123",
#             "name": "access.log",
#         },
#         {
#             "type": "dir1",
#             "size": "123",
#             "name": "access.log.gz",
#         },
#         {
#             "type": "dir",
#             "size": "123",
#             "name": "error.log",
#         },
#         {
#             "type": "dir",
#             "size": "157",
#             "name": "access-auth.log",
#         },
#     ]
#     # 搜索关键字
#     va = "dir1"
#     result = fuzzyutil().fuzzy_finder(va, 'type', file_list)
#     print(result)

