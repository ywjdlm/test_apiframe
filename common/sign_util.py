#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib


class signutil():


    #筛选传输数据,sign或者参数名的值为空的值直接忽略,最后返回一个含参数值和名称的列表
    def GetSignData(self,data):
        try:
            #定义一个空的字典
            signData = {}
            #获取传输字典的键和值
            for key, value in data.items():
                # 去除无法组建sign的键值,重新返回一个新的可拼接的字典格式
                if value != "" and value != "null" and key != "sign":
                    signData[key] = value
            return signData
        # print(signData)
        except:
            raise Exception('传参格式不为字典格式,请检查!!!')


    #根据筛选后的传参数据生成MD5加密格式的字符串
    def SignString(self,data):
        signData = signutil().GetSignData(data)#调用GetSignData方法获取非空的参数名以及参数值,返回一个字典格式的数据
        #将筛选后的data的参数名列成列表
        list = signData.keys()
        #定义一个空字符串
        stringA = ''
        #拼接成参数名=参数值&....&参数名N=参数值N的格式
        for i in list:
            #判断数据的值是否是整数型,若为整数型则转换为字符串进行拼接
            if type(signData[i])==int:
                signData[i]=str(signData[i])
            stringA = stringA + i + "=" + signData[i] + "&"
        #截取全新字符串,去掉"&"符号
        stringA = stringA[0:-1]
        #视情况,若需要增加sign_key则注释 stringA = stringA[0:-1]即可
        #stringA =stringA+ "sign_key" + "=" + "4ef7692d629fc3760ef432cb772b9ed0"
        return stringA

    #根据MD5传参字符串格式进行加密,返回MD5加密后的大写字符串
    def getsign(self,data):

        signstring=signutil().SignString(data)
        # 创建MD5
        md = hashlib.md5()
        # 对stringA字符串进行编码
        md.update(signstring.encode('utf-8'))
        # 数据加密
        signValue = md.hexdigest()
        # 把加密的结果，小写转换成大写，upper函数
        signValue = signValue.upper()
        return signValue


if __name__ == '__main__':
    alldata = {
        "content": "哦哦哦哦",
        "image": "http://static.rulin49.com/055ef6397ec8d2ef6308ee35acf4108b.jpg?w=1334&h=750 ",
        "labelId": "49",
        "locationId": "60a8c64c91a04c4d98ccf48ac51243d8",
        "sign": "00612E7A9FFDFF2C24284BC89E9A35DA",
        "type": "6",
        "bid":'null',
        "num":"",
        'phone':1571754405
    }

    data=['sign','','null']
    print(signutil().SignString(alldata))
    print("==========================================================================================")
    a=signutil().getsign(alldata)
    print(a)

