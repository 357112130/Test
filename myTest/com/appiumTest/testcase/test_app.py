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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from PIL import Image
from PIL import ImageEnhance
import pytesseract
from myTest.com.appiumTest.data.data import connect_config, desired_caps, user_data, state_condition, path


class AppTest(unittest.TestCase):

	# 开始前执行的方法
	def setUp(self):
		# 连接Appium
		self.driver = webdriver.Remote(connect_config["appiumServe"], desired_caps)
		print(state_condition["connect_appiumSucess"] + "...")
		self.driver.implicitly_wait(6)

	# 执行用例
	def test_option(self):
		# 进行注册操作
		self.driver.find_element_by_id("loginNewUser").click()  # 点击新用户注册
		sleep(1)
		# 输入注册信息
		self.driver.find_element_by_id("registerId").clear()
		self.driver.find_element_by_id("registerId").send_keys(user_data["username"])  # 手机号
		sleep(1)
		self.driver.find_element_by_id("registerPassword").clear()
		self.driver.find_element_by_id("registerPassword").send_keys(user_data["password"])  # 密码
		sleep(1)
		self.driver.find_element_by_id("turePassword").clear()
		self.driver.find_element_by_id("turePassword").send_keys(user_data["password"])  # 密码
		sleep(1)
		# 获取验证码
		self.driver.save_screenshot(path["yzm_path"] + "image_old.png")  # 截图保存
		# 打开截图,获取验证码位置,截取保存验证码
		ran = Image.open(path["yzm_path"] + "image_old.png")
		box = (29, 740, 529, 861)  # 左,上,右,下
		ran.crop(box).save(path["yzm_path"] + "image_new.png")
		sleep(2)
		img = Image.open(path["yzm_path"] + "image_new.png")  # 根据地址,读取图片
		imgry = img.convert()  # 图像加强,二值化
		sharpness = ImageEnhance.Contrast(imgry)  # 增强对比度
		sharp_img = sharpness.enhance(2.0)
		sharp_img.save(path["yzm_path"] + "image_yzm.png")  # 将处理后的图片保存
		sharp_img.load()  # 增强对比度
		sleep(2)
		image = Image.open(path["yzm_path"] + "image_yzm.png")  # 打开处理后的图片
		code = pytesseract.image_to_string(image)  # 读取里面的内容
		print(code)
		# 输入验证码
		# self.driver.find_element_by_id("registerAuth").clear()
		# self.driver.find_element_by_id("registerAuth").send_keys(code)
		sleep(10)
		# 点击注册按钮
		self.driver.find_element_by_id("registerBtn").click()
		print(state_condition["registerSuccess"] + "...")
		sleep(1)
		# 断言注册成功
		if ui.WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "message"))):
			register_success_msg = self.driver.find_element_by_id("message").text
			print(register_success_msg)
			if self.assertIn(state_condition["registerSuccess"], register_success_msg):
				print(state_condition["toLogin"] + "...")
			else:
				self.driver.get_screenshot_as_file(path["error_path"] + "error_register.jpg")
				print(state_condition["registerFailed"] + "...")
		else:
			print("元素不可见")
		# 注册成功,点击确认按钮跳转到登录界面
		self.driver.find_element_by_id("button1").click()
		sleep(3)

		# 进行登录操作
		self.driver.find_element_by_id("loginId").clear()
		self.driver.find_element_by_id("loginId").send_keys(user_data["username"])  # 手机号
		self.driver.find_element_by_id("loginPassword").clear()
		self.driver.find_element_by_id("loginPassword").send_keys(user_data["password"])  # 密码
		# 点击登录按钮
		self.driver.find_element_by_id("loginBtn").click()
		# 断言登录成功
		user = self.driver.find_element_by_id("loginId").text
		pwd = self.driver.find_element_by_id("loginPassword").text
		print(user, pwd)
		if self.assertIn(user_data["username"], user) and self.assertIn(user_data["password"], pwd):
			print(state_condition["loginSuccess"])
		else:
			self.driver.get_screenshot_as_file(path["error_path"] + "error_login.jpg")
			print(state_condition["loginFailed"])
		sleep(3)

	# 测试结束后关闭
	def tearDown(self):
		self.driver.quit()
