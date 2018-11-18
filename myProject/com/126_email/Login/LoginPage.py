# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/28 17:38
# @File: LoginPage.py
# @Description:
# @Modified By:
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()


class LoginPage:
	# 定义变量
	def defining_variable(self):
		variable = {
			"${URL}": "https://mail.126.com/",
			"${USERNAME}": "idInput",
			"${PASSWORD}": "pwdInput",
			"${LOGIN_BTN}": "loginBtn"
		}

	# 获取用户名输入框
	def login_UserName(self):
		element = driver.find_element_by_id("${USERNAME}")

	# 获取密码输入框
	def login_Password(self):
		element = driver.find_element_by_id("${PASSWORD}")

	# 获取登录按钮
	def login_Button(self):
		elemnet = driver.find_element_by_id("${LOGIN_BTN}")

	def open(self):
		driver.get("${URL}")
		driver.maximize_window()


if __name__ == '__main__':
	LoginPage.open()
