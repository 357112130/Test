# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/25 20:54
# @File: practice4.py
# @Description:
# @Modified By:
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("upfile.html")
driver.get(file_path)
sleep(2)
driver.find_element_by_name("file").send_keys("C:\Users\Administrator\Desktop\up.txt")
sleep(10)
driver.quit()
