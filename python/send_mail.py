#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 465  # port
mail_user = "78180486@qq.com"  # 用户名
mail_pass = input('输入密码！')  # 口令

sender = '78180486@qq.com'
receivers = ['swrd168@163.com','swrd1688@163.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('邮件内容：Python邮件发送测试...', 'plain', 'utf-8')
message['From'] = formataddr(["From yy", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To'] = formataddr(["To yyqq", ''])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
message['Subject'] = "Python SMTP 邮件测试"  # 邮件的主题，也可以说是标题

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件\n",e)
