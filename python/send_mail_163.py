#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_port = 465  # port
mail_user = "swrd168@163.com"  # 用户名
mail_pass = input('输入密码！')  # 口令

sender = 'swrd168@163.com'
receivers = ['78180486@qq.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#邮件内容和标题最好写的正式点，163邮箱的反垃圾邮件会自动拦击垃圾邮件，导致发送失败
content='邮件内容：Python邮件发送测试... \nconda非常方便的管理工具包，以及支持不同版本python的环境；\npycharm主要是个好用的编辑器conda非常方便的管理工具包，以及支持不同版本python的环境；pycharm主要是个好用的编辑器\n'
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = formataddr(["From yy", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To'] = formataddr(["To yyqq", '78180486@qq.com'])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
message['Subject'] = "Python SMTP 发送邮件测试"  # 邮件的主题，也可以说是标题

try:
    smtpObj = smtplib.SMTP_SSL(mail_host,mail_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件\n",e)
