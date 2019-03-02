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

	# self.driver.switch_to.default_content()

	def test_login_sucess(self):
		# 用户名和密码正确
		self.login("357112130@qq.com", "aptx_48691")
		sleep(10)
		link = self.driver.find_element_by_id("useralias").text
		print(link)
		# 断言用户登录成功验证是否存在
		self.assertTrue("凌辰" in link)

	def test_login_username_error(self):
		# 用户名错误,密码正确
		self.login("错误的用户名", "aptx_48691")
		sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		print(error_message)
		# 断言错误的用户名tips=error_message
		self.assertIn("", error_message)
		# self.assertIn("输入正确的", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_username_error.jpg")

	def test_login_password_error(self):
		# 用户名正确,密码错误
		self.login("2214571423@qq.com", "aptx_486")
		sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		print(error_message)
		# 断言错误的密码tips=error_message
		self.assertIn("", error_message)
		# self.assertIn("输入的帐号或密码不正确", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_password_error.jpg")

	def test_login_username_null(self):
		# 用户名为空,密码正确
		self.login("", "aptx_48691")
		sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		print(error_message)
		# 断言用户名为空tips=error_message
		self.assertIn("", error_message)
		# self.assertIn("没有输入帐号", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_username_null.jpg")

	def test_login_password_null(self):
		# 用户名正确,密码为空
		self.login("357112130@qq.com", "")
		sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		print(error_message)
		# 断言密码为空tips=error_message
		self.assertIn("", error_message)
		# self.assertIn("你还没有输入密码", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_password_null.jpg")


if __name__ == '__main__':
	unittest.main
