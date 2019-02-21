# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description:
# @date: create in 2019/1/27 20:18
# @file：LoginBasePage.py
# @modified By:
from selenium import webdriver
from time import sleep
from CMS.com.test_module.common.CommonBasePage import CommonBasePage


class LoginBasePage():

	# 用户登录
	def user_login(self, driver, login_username, login_password):
		driver.find_element_by_name("username").clear()
		driver.find_element_by_name("username").send_keys(login_username)
		driver.find_element_by_name("password").clear()
		driver.find_element_by_name("password").send_keys(login_password)
		driver.find_element_by_name("Submit").submit()
		sleep(3)

	# 用户退出
	def user_logout(self, driver):
		driver.find_element_by_link_text("退出").click()
		driver.switch_to_alert().accept()
		sleep(3)
		driver.close()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	CommonBasePage().common(driver)

	LoginBasePage().user_login(driver, "test", "123456")
	LoginBasePage().user_logout(driver)
