# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/25 21:17
# @File: practice6.py
# @Description:
# @Modified By:
from selenium import webdriver
from time import sleep

# window.scrollTo(左边距,上边距)
# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(800, 500)
sleep(2)
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)
driver.quit()
