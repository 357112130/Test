# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/3 15:13
# @file：test_app.py
# @modified By:
from time import sleep
from appium import webdriver
import unittest


class MyTests(unittest.TestCase):

	# 测试开始前执行的方法
	def setUp(self):
		desired_caps = {'platformName': 'Android',  # 平台名称
						'platformVersion': '4.4.2',  # 系统版本号
						'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
						'appPackage': 'com.example.androidtest',  # apk的包名
						'appActivity': 'com.fg.androidtest.activty.LoginActivity'  # activity 名称
						}
		self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
		self.driver.implicitly_wait(8)

	# 执行case
	def test_input(self):
		self.driver.find_element_by_id("loginId").send_keys("18370763232")
		self.driver.find_element_by_id("loginPassword").send_keys("aptx_4869")
		self.driver.find_element_by_id("loginBtn").click()
		sleep(2)

	# 测试结束后执行的方法
	def tearDown(self):
		self.driver.quit()
