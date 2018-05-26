#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "gujientsy@163.com"  # 用户名
mail_pass = "86917307x"  # 口令

sender = 'gujientsy@163.com'
receivers = ['1216933842@qq.com','gujie1216933842@sina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送...', 'plain', 'utf-8')
message['From'] = 'gujientsy@163.com'
message['To'] = '1216933842@qq.com'

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号 ,注意:阿里云服务器上 25端口被禁用了,在阿里云上执行会显示超时
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException as e:
    print('异常:%s' % (e))
    print("Error: 无法发送邮件")
