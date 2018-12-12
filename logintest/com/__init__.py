# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2018/12/12 20:08
# @file：__init__.py.py
# @modified By:
import unittest
from selenium import webdriver
import time


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
		self.driver.find_element_by_id("u").send_keys(username)
		self.driver.find_element_by_id("p").send_keys(password)
		self.driver.find_element_by_id("login_button").click()

	def test_login_sucess(self):
		'''用户名和密码正确'''
		self.login("357112130@qq.com", "aptx_48691")  # 正确的用户名和密码
		time.sleep(10)
		link = self.driver.find_element_by_id()
		self.assertTrue("" in link.text)  # 断言用户登录成功验证是否存在

	def test_login_username_error(self):
		'''用户名错误,密码正确'''
		self.login("357112130", "aptx_48691")  # 错误的用户名
		time.sleep(10)
		error_message = self.driver.find_element_by_id("").text
		self.assertIn("", error_message)  # 断言错误的用户名tips=error_message
		self.driver.get_screenshot_as_file("D:\\pyProject\\logintest\com\\testcase\\login_username_error.jpg")  # 截图

	def test_login_password_error(self):
		'''用户名正确,密码错误'''
		self.login("357112130@qq.com", "aptx_4869")  # 错误的密码
		time.sleep(10)
		error_message = self.driver.find_element_by_id("").text
		self.assertIn("", error_message)  # 断言错误的密码tips=error_message
		self.driver.get_screenshot_as_file("D:\\pyProject\\logintest\com\\testcase\\login_password_error.jpg")  # 截图

	def test_login_username_null(self):
		'''用户名为空,密码正确'''
		self.login("357112130@qq.com", "")  # 用户名为空
		time.sleep(10)
		error_message = self.driver.find_element_by_id("").text
		self.assertEqual(error_message, "")  # 断言用户名为空tips=error_message
		self.driver.get_screenshot_as_file("D:\\pyProject\\logintest\com\\testcase\\login_username_null.jpg")  # 截图

	def test_login_password_null(self):
		'''用户名正确,密码为空'''
		self.login("357112130@qq.com", "")  # 密码为空
		time.sleep(10)
		error_message = self.driver.find_element_by_id("").text
		self.assertEqual(error_message, "")  # 断言密码为空tips=error_message
		self.driver.get_screenshot_as_file("D:\\pyProject\\logintest\com\\testcase\\login_password_null.jpg")  # 截图

if __name__ == '__main__':
    unittest.main