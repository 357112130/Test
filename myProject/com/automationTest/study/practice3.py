# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/24 21:12
# @File: practice3.py
# @Description:
# @Modified By:
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
driver.maximize_window()
# 鼠标悬停至“设置”链接
set_up = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(set_up).perform()
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
# 保存设置
save_set_up = driver.find_element_by_class_name("prefpanelgo")
if save_set_up.is_displayed():
    save_set_up.click()
sleep(10)
try:
    alert = driver.switch_to.alert
    alert.text
    driver.switch_to.alert.accept()
except NoAlertPresentException:
    pass
# 接受警告框
# driver.switch_to.alert.accept()
# sleep(2)
# # 搜索结果显示条数
# sel = driver.find_element_by_xpath("//select[@id='nr']")
# if sel.is_displayed():
#     Select(sel).select_by_value('50')  # 显示50条

sleep(2)
driver.quit()
