# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/2/21 20:24
# @file：CommonBasepage.py
# @modified By:
from selenium import webdriver
from time import sleep


class CommonBasePage():

	def common(self, driver):
		driver.get("http://localhost")
		driver.maximize_window()
