# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/24 20:39
# @File: practice2.py
# @Description:
# @Modified By:
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath("//div/h3/a")

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.back()
driver.implicitly_wait(10)
# 获取百度搜索窗口句柄
search_handles = driver.current_window_handle
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()
# 获取当前所有打开的窗口句柄
all_handles = driver.window_handles
# 进入注册窗口
for handle in all_handles:
    if handle != search_handles:
        driver.switch_to_window(handle)
        print ("注册窗口")
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("password").send_keys("password")

sleep(3)
driver.quit()
