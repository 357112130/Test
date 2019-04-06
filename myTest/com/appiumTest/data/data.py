# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/16 20:23
# @file：data.py
# @modified By:

# 配置说明
connect_config = {
	"appiumServe": "http://127.0.0.1:4723/wd/hub"
}
desired_caps = {"platformName": "Android",  # 平台名称
				"platformVersion": "5.1.1",  # 系统版本号
				"deviceName": "127.0.0.1:62001",  # 设备名称。如果是真机，在"设置->关于手机->设备名称"里查看
				"appPackage": "com.example.androidtest",  # apk的包名
				"appActivity": "com.fg.androidtest.activty.LoginActivity"  # activity 名称
				}
user_data = {
	"username": "18370763232",
	"password": "aptx_4869"
}
state_condition = {
	"connect_appiumSucess": "连接Appium成功",
	"registerSuccess": "注册成功！",
	"registerFailed": "注册失败",
	"toLogin": "正在跳转到登录界面",
	"loginSuccess": "登录成功",
	"loginFailed": "登录失败"
}
path = {
	"yzm_path": "D://pyProject//myTest//com//appiumTest//image//verification_code//",
	"error_path": "D://pyProject//myTest//com//appiumTest//image//screenshot_error//"
}
report_data = {
	"title": "python+appium自动化测试报告",
	"desc": "用例执行情况:"
}
