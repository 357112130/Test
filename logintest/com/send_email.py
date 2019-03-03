# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/2 18:28
# @file：send_email.py
# @modified By:
import smtplib
# import os.path as pth
import time
from email.mime.text import MIMEText
from email.header import Header


def sendEmail(content, title, from_name, from_address, to_address, serverport, serverip, username, password):
	msg = MIMEText(content, _subtype="html", _charset="utf-8")
	msg['Subject'] = Header(title, "utf-8")
	# 这里的to_address只用于显示，必须是一个string
	msg['To'] = ','.join(to_address)
	msg['From'] = from_name
	try:
		s = smtplib.SMTP_SSL(serverip, serverport)
		s.login(username, password)
		# 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
		s.sendmail(from_address, to_address, msg.as_string())
		print('%s----发送测试报告邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	except Exception as error:
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		print(error)


# HEFEN_D = pth.abspath(pth.dirname(__file__))

def mains():
	TO = ['2634772529@qq.com']
	config = {
		"from": "357112130@qq.com",
		"from_name": '自动化测试unittest测试框架报告:',
		"to": TO,
		"serverip": "smtp.qq.com",
		"serverport": "465",#465 587
		"username": "357112130@qq.com",
		"password": "plwuyrlmwcvpcajj"  # QQ邮箱的SMTP授权码
	}

	title = u"自动化测试unittest测试框架报告"
	f = open("D://pyProject//logintest//com//testcase//report//result_logintest.html", "rb")
	mail_body = f.read()
	f.close()
	sendEmail(mail_body, title, config['from_name'], config['from'], config['to'], config['serverport'],
			  config['serverip'], config['username'], config['password'])

if __name__ == '__main__':
    mains()