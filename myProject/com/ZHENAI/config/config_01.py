# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/10 9:48
# @file：config_01.py
# @modified By:
from selenium import webdriver
from selenium.webdriver.common.action_chains import *

# 浏览器
browser_config = {
	"chrome": webdriver.Chrome,
	"firefox": webdriver.Firefox
}

# 定位信息
location_config = {
	u"珍爱网首页": {
		u"性别女": ["xpath", "/html/body/section/div[2]/div/section/section/div/div[2]/div/div[2]/div"],
		u"1996年": ["xpath",
				   "//section[@id='app']/div[2]/div/section/section/div[2]/div[2]/div/div/div/div[2]/div[2]/div[7]"],
		u"11月": ["xpath",
				 "//section[@id='app']/div[2]/div/section/section/div[2]/div[2]/div/div/div[2]/div[2]/div[12]"],
		u"22日": ["xpath",
				 "//section[@id='app']/div[2]/div/section/section/div[2]/div[2]/div/div/div[3]/div[2]/div[23]"],
		u"江西省": ["xpath",
				 "//section[@id='app']/div[2]/div/section/section/div[3]/div[2]/div/div/div/div[2]/div/div[20]"],
		u"赣州市": ["xpath", "//section[@id='app']/div[2]/div/section/section/div[3]/div[2]/div/div/div[2]/div[2]/div[8]"],
		u"南康区": ["xpath", "//section[@id='app']/div[2]/div/section/section/div[3]/div[2]/div/div/div[3]/div[2]/div[3]"],
		u"注册按钮": ["xpath", "/html/body/section/div[2]/div/section/div[2]/div/div"],
	}
}
