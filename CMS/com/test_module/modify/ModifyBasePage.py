# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/2/11 19:56
# @file：ModifyBasePage.py
# @modified By:
from selenium import webdriver
from time import sleep


class ModifyBasePage():

	# 修改基本资料
	def data_modify(self, truename, qq_number, msn, mycall, phone_number, website_address, family_address, zip_code,
					personal_introduction):
		driver.find_element_by_link_text(u"修改资料").click()
		sleep(1)
		driver.find_element_by_id("truename").send_keys(truename)
		driver.find_element_by_id("oicq").send_keys(qq_number)
		driver.find_element_by_id("msn").send_keys(msn)
		driver.find_element_by_id("mycall").send_keys(mycall)
		driver.find_element_by_id("phone").send_keys(phone_number)
		driver.find_element_by_id("homepage").send_keys(website_address)
		driver.find_element_by_id("address").send_keys(family_address)
		driver.find_element_by_id("zip").send_keys(zip_code)
		driver.find_element_by_id("saytext").send_keys(personal_introduction)
		sleep(3)
		driver.find_element_by_link_text(u"修改信息").click()

	# 修改密码
	def password_modify(self, old_pwd, new_pwd, confirm_pwd, new_email):
		driver.find_element_by_link_text(u"修改安全信息").click()
		sleep(1)
		driver.find_element_by_id("oldpassword").send_keys(old_pwd)
		driver.find_element_by_id("password").send_keys(new_pwd)
		driver.find_element_by_id("repassword").send_keys(confirm_pwd)
		driver.find_element_by_id("email").send_keys(new_email)
		sleep(3)
		driver.find_element_by_link_text(u"修改信息").click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("http://localhost")

	driver.find_element_by_link_text(u"普通会员").click()
