#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.ini_util import iniutil


class sendmailutil():
    """
    email_to:邮件接收者地址
    filepath:需要传入的附件
    """


    def send_mail(self,email_to,filepath):
        # sendaddr = "1571754405@qq.com"
        # QQ_pwd = 'fbbpohhkqbquigjf'
        sendaddr =iniutil().get_confini('mail','sendaddr')
        QQ_pwd = iniutil().get_confini('mail','QQ_pwd')
        now = time.strftime('%Y-%m-%d  %H:%M:%S')  # 获取时间戳

        #主题
        msg = MIMEMultipart()
        msg["Subject"] = now + "测试报告"  #标题
        msg["From"] = sendaddr  #邮件发送者
        msg["To"] = email_to    #邮件接收者

        #文字部分,内容
        part = MIMEText("本次接口自动化测试报告，请查收!!!", 'plain', 'utf-8')  # 汉字防止出现乱码
        msg.attach(part)

        # 附件部分，只能发一个附件，需要多个附件，对下面代码做for循环
        part = MIMEApplication(open(filepath, "rb").read())  # 打开附件
        part.add_header("Content-Disposition", "attachment", filename=filepath)  # 添加头部信息
        msg.attach(part)

        #多个附件
        # path = ["附件地址1","附件地址2","附件地址3".....]
        # for item in path:
        #     part = MIMEApplication(open(item, "rb").read())
        #     part.add_header("Content-Disposition", "attachment", filename=filepath)
        #     msg.attach(part)

        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", timeout=30)  # 连接SMTP邮件服务，默认端口是25
            s.login(sendaddr, QQ_pwd)  # 登录服务器
            s.sendmail(sendaddr, email_to, msg.as_string())  # 发送邮件
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")



# if __name__ == '__main__':
#     sendmailutil().send_mail("980975647@qq.com",r"C:\Users\Administrator\Desktop\测试用例-员工宝.xlsx")
#     sendmailutil().send_mail("1571754405@qq.com",r"C:\Users\Administrator\Desktop\测试用例-员工宝.xlsx")
#     print("配置文件调试成功")

