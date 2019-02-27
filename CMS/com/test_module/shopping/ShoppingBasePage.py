# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/2/20 20:07
# @file：ShoppingBasePage.py
# @modified By:
from selenium import webdriver
from time import sleep
from CMS.com.test_module.common.CommonBasePage import CommonBasePage
from CMS.com.test_module.login.LoginBasePage import LoginBasePage


class ShoppingBasePage():

	# 购买电脑
	def buy_computers(self, driver, computer_name, truename, mycall, family_address):
		driver.find_element_by_id("tabnav_btn_4").click()
		sleep(1)
		# 点击该电脑链接进入详情
		driver.find_element_by_link_text(computer_name).click()
		# 打印该电脑配置信息
		computer_message = driver.find_element_by_id("text").text
		print (u"电脑详情:\n" + computer_message)
		# 点击加入购物车
		driver.find_element_by_xpath(
			"/html/body/table[4]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/a[1]").click()
		sleep(1)
		# 获取当前窗口句柄
		currentWindow = driver.current_window_handle
		# 获取所有窗口的句柄
		handles = driver.window_handles
		for handle in handles:
			if handle != currentWindow:
				# 将driver与新的页面绑定
				driver.switch_to.window(handle)
				driver.maximize_window()
		# 点击下一步
		driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/div/a[3]").click()
		# 填写收货人信息(带*选项为必选)
		driver.find_element_by_id("truename").clear()
		driver.find_element_by_id("truename").send_keys(truename)
		driver.find_element_by_id("mycall").clear()
		driver.find_element_by_id("mycall").send_keys(mycall)
		driver.find_element_by_id("address").clear()
		driver.find_element_by_id("address").send_keys(family_address)
		# 点击下一步继续
		driver.find_element_by_name("Submit").click()
		# 打印收货人信息
		receiving_message = driver.find_element_by_xpath("//*[@id='myorder']/table/tbody/tr[5]/td/table/tbody").text
		print (u"收货人信息:\n" + receiving_message)
		# 点击提交订单
		driver.find_element_by_name("Submit").click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	CommonBasePage().common(driver)
	LoginBasePage().user_login(driver, "test", "123456")
	sleep(2)
	ShoppingBasePage().buy_computers(driver, u"华硕笔记本A8H233sc-DR(90NNKXAI131815AN", u"凌辰", "6685617", "here")

	driver.implicitly_wait(3)
	alipay = driver.find_element_by_id("QuickLinksMore1").text
	if alipay == u"哇！支付宝":
		sleep(2)
		driver.quit()
