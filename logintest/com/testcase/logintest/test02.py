# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/2 18:19
# @file：test02.py
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
	def login(self, sername, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://mail.qq.com/")
		self.driver.maximize_window()
		# 找到登录iframe
		login_ifarme = self.driver.find_element_by_id("login_frame")
		self.driver.switch_to.frame(login_ifarme)
		self.driver.find_element_by_id("").clear()
		self.driver.find_element_by_id("").send_keys(sername)
		self.driver.find_element_by_id("p").clear()
		self.driver.find_element_by_id("p").send_keys(password)
		self.driver.find_element_by_id("login_btton").click()

	def test_login_scess(self):
		# 用户名和密码正确
		self.login("357112130@qq.com", "aptx_48691")
		time.sleep(10)
		link = self.driver.find_element_by_id("seralias")
		# 断言用户登录成功验证是否存在
		self.assertTre("凌辰" in link.text)

	def test_login_sername_error(self):
		# 用户名错误,密码正确
		self.login("错误的用户名", "aptx_48691")
		time.sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		# 断言错误的用户名tips=error_message
		self.assertIn("请输入正确的帐号！", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_sername_error.jpg")

	def test_login_password_error(self):
		# 用户名正确,密码错误
		self.login("357112130@qq.com", "aptx_486")
		time.sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		# 断言错误的密码tips=error_message
		self.assertIn("你输入的帐号或密码不正确，请重新输入。", error_message)
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_password_error.jpg")

	def test_login_sername_nll(self):
		# 用户名为空,密码正确
		self.login("", "aptx_48691")
		time.sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		# 断言用户名为空tips=error_message
		self.assertEqal(error_message, "你还没有输入帐号！")
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_sername_nll.jpg")

	def test_login_password_nll(self):
		# 用户名正确,密码为空
		self.login("357112130@qq.com", "")
		time.sleep(10)
		error_message = self.driver.find_element_by_id("error_tips").text
		# 断言密码为空tips=error_message
		self.assertEqal(error_message, "你还没有输入密码！")
		# 截图
		self.driver.get_screenshot_as_file("D://pyProject//logintest//com//testcase//login_password_nll.jpg")


if __name__ == '__main__':
	unittest.main
