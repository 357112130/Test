# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/2 18:19
# @file：test02.py
# @modified By:
import unittest
from selenium import webdriver
from time import sleep


class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("开始测试")

	@classmethod
	def tearDownClass(cls):
		print("结束测试")

	def setUp(self):
		print("开始单个测试用例")

	def tearDown(self):
		print("结束单个测试用例")

	# 定义登录方法
	def login(self, username, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://mail.qq.com/")
		self.driver.maximize_window()
		# 找到登录iframe
		login_iframe = self.driver.find_element_by_id("login_frame")
		self.driver.switch_to.frame(login_iframe)
		self.driver.find_element_by_id("u").clear()
		self.driver.find_element_by_id("u").send_keys(username)
		self.driver.find_element_by_id("p").clear()
		self.driver.find_element_by_id("p").send_keys(password)
		self.driver.find_element_by_id("login_button").click()

	# 用户名和密码正确
	def test_login_sucess(self):
		self.login("357112130@qq.com", "aptx_48691")
		sleep(2)
		link = self.driver.find_element_by_id("useralias").text
		print(link)
		# 断言用户登录成功验证是否存在
		self.assertTrue("凌辰" in link)

	# 用户名错误,密码正确
	def test_login_username_error(self):
		self.login("错误的用户名", "aptx_48691")
		sleep(2)
		error_message = self.driver.find_element_by_id("err_m").text
		print(error_message)
		# 断言错误的用户名tips=error_message
		self.assertIn("请输入正确的帐号！", error_message)
		# 截图
		self.driver.get_screenshot_as_file(
			"D://pyProject//logintest//com//testcase//screenshot_error//login_username_error.jpg")

	# 用户名正确,密码错误
	def test_login_password_error(self):
		self.login("2214571423@qq.com", "aptx_486")
		sleep(2)
		error_message = self.driver.find_element_by_id("err_m").text
		print(error_message)
		# 断言错误的密码tips=error_message
		self.assertIn("你输入的帐号或密码不正确，请重新输入。", error_message)
		# 截图
		self.driver.get_screenshot_as_file(
			"D://pyProject//logintest//com//testcase//screenshot_error//login_password_error.jpg")

	# 用户名为空,密码正确
	def test_login_username_null(self):
		self.login("", "aptx_48691")
		sleep(2)
		error_message = self.driver.find_element_by_id("err_m").text
		print(error_message)
		# 断言用户名为空tips=error_message
		self.assertIn("你还没有输入帐号！", error_message)
		# 截图
		self.driver.get_screenshot_as_file(
			"D://pyProject//logintest//com//testcase//screenshot_error//login_username_null.jpg")

	# 用户名正确,密码为空
	def test_login_password_null(self):
		self.login("357112130@qq.com", "")
		sleep(2)
		error_message = self.driver.find_element_by_id("error_tips").text
		print(error_message)
		# 断言密码为空tips=error_message
		self.assertIn("你还没有输入密码！", error_message)
		# 截图
		self.driver.get_screenshot_as_file(
			"D://pyProject//logintest//com//testcase//screenshot_error//login_password_null.jpg")


if __name__ == '__main__':
	unittest.main
