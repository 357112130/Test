# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/1/27 20:52
# @file：RegisterBasePage.py
# @modified By:
from selenium import webdriver
from time import sleep
from CMS.com.test_module.common.CommonBasePage import CommonBasePage


class RegisterBasePage():

	# 普通会员注册
	def ordinary_register(self, driver, o_register_username, o_register_password, o_register_repassword,
						  o_register_email):
		driver.find_element_by_name("button").click()
		driver.find_element_by_id("username").send_keys(o_register_username)
		driver.find_element_by_id("password").send_keys(o_register_password)
		driver.find_element_by_id("repassword").send_keys(o_register_repassword)
		driver.find_element_by_id("email").send_keys(o_register_email)
		sleep(1)
		driver.find_element_by_name("Submit").click()
		sleep(3)

	# 企业会员注册
	def enterprise_register(self, driver, e_register_username, e_register_password, e_register_repassword,
							e_register_email, e_register_company, e_register_truename, e_register_mycall):
		driver.find_element_by_xpath("//input[@value='3']").click()
		driver.find_element_by_name("button").click()
		sleep(1)
		driver.find_element_by_id("username").send_keys(e_register_username)
		driver.find_element_by_id("password").send_keys(e_register_password)
		driver.find_element_by_id("repassword").send_keys(e_register_repassword)
		driver.find_element_by_id("email").send_keys(e_register_email)
		driver.find_element_by_id("company").send_keys(e_register_company)
		driver.find_element_by_id("truename").send_keys(e_register_truename)
		driver.find_element_by_id("mycall").send_keys(e_register_mycall)
		sleep(1)
		driver.find_element_by_name("Submit").click()
		sleep(3)


if __name__ == '__main__':
	driver = webdriver.Chrome()
	CommonBasePage().common(driver)

	# 获取当前窗口句柄
	currentWindow = driver.current_window_handle
	driver.find_element_by_name("Submit2").click()
	sleep(1)

	# 获取所有窗口的句柄
	handles = driver.window_handles
	for handle in handles:
		if handle != currentWindow:
			# 将driver与新的页面绑定
			driver.switch_to.window(handle)

	# RegisterBasePage().ordinary_register(driver, "test1", "123456", "123456", "test1@qq.com")

	RegisterBasePage().enterprise_register(driver, "test2", "123456", "123456", "test2@qq.com", u"帝国", u"凌辰",
										   "12345678901")
	driver.implicitly_wait(3)
	driver.quit()
