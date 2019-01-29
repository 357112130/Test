# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/1/28 20:51
# @file：test.py
# @modified By:
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.maximize_window()

currentWindow = driver.current_window_handle

driver.find_element_by_name("Submit2").click()
sleep(1)

handles = driver.window_handles
print (handles)

for handle in handles:
	if handle != currentWindow:
		driver.switch_to.window(handle)
currentWindow = driver.current_window_handle
driver.find_element_by_name("button").click()
