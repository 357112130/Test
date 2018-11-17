#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
# 键盘操作
from selenium.webdriver.common.keys import Keys
# 等待
from selenium.webdriver.support.ui import WebDriverWait
# 当前时间
from time import ctime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time

driver = webdriver.Chrome()
driver.maximize_window()
firstUrl = "http://www.baidu.com"
secondUrl = "http://news.baidu.com"
driver.implicitly_wait(10)
driver.get(firstUrl)
action = ActionChains(driver)
inputs = driver.find_element_by_id("kw")
btn = driver.find_element_by_id("su")

# "第9 "
# 显式等待
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver ：浏览器驱动。
# timeout ：最长超时时间，默认以秒为单位。
# poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
# ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。
# element = WebDriverWait(driver,5,0.5).until(EC.preence_of_element_located(By.ID,"kw"))
# element.send_keys("selenium")

# 隐式等待
try:
    print (ctime())
    driver.find_element_by_id("kw2").send_keys("selenium")
except NoSuchElementException as error:
    print (error)
finally:
    print (ctime())

# def t1():
#     driver.get(firstUrl)
#     print ("now access %s" % (firstUrl))
#     time.sleep(2)
#     driver.get(secondUrl)
#     print ("now access %s" % (secondUrl))
#     time.sleep(2)
#     print ("back to  %s " % (firstUrl))
#     driver.back()
#     time.sleep(1)
#     print ("forward to  %s" % (secondUrl))
#     driver.forward()
#     time.sleep(3)
#     driver.refresh()
#     time.sleep(5)

# def t2():
#     driver.get(firstUrl)
#     driver.find_element_by_id("kw").send_keys("aaaaaaaa")
#     driver.find_element_by_id("kw").clear()
#     time.sleep(3)
#     driver.find_element_by_id("kw").send_keys("t2")
#     driver.find_element_by_id("su").click()

# def t3():
#     size = driver.find_element_by_id("kw").size
#     print (size)
#     time.sleep(3)
#     text = driver.find_element_by_id("cp").text
#     print (text)
#     time.sleep(3)
#     # 类型
#     attribute = driver.find_element_by_id("kw").get_attribute("type")
#     print (attribute)
#     time.sleep(3)
#     # 是否可见
#     result = driver.find_element_by_id("kw").is_displayed()
#     print (result)
#     time.sleep(3)

# def t4():
#     above = driver.find_element_by_link_text("设置")
#     action.move_to_element(above).perform()
#     time.sleep(3)
#     r1 = driver.find_element_by_link_text("地图")
#     action.context_click(r1).perform()
#     time.sleep(3)
#     ll = driver.find_element_by_link_text("hao123")
#     action.double_click(ll).perform()
#     time.sleep(3)
#     driver.back()
#     time.sleep(1)
#     r = driver.find_element_by_link_text("新闻")
#     action.drag_and_drop(r, inputs).perform()
#     time.sleep(3)

# def t5():
#     inputs.send_keys("studys")
#     time.sleep(1)
#     inputs.send_keys(Keys.BACK_SPACE)
#     time.sleep(1)
#     inputs.send_keys(Keys.SPACE)
#     time.sleep(1)
#     inputs.send_keys(u"学习")
#     time.sleep(1)
#     inputs.send_keys(Keys.CONTROL, "a")
#     time.sleep(1)
#     inputs.send_keys(Keys.CONTROL, "x")
#     time.sleep(1)
#     inputs.send_keys(Keys.CONTROL, "v")
#     time.sleep(1)
#     btn.send_keys(Keys.ENTER)
#     time.sleep(1)

# def t6():
#     print ("Before Search======")
#     title1 = driver.title
#     print (title1)
#     time.sleep(2)
#     nowUrl1 = driver.current_url
#     print ("nowUrl1=" + nowUrl1)
#     time.sleep(2)
#     inputs.send_keys("selenium")
#     btn.click()
#     time.sleep(2)
#     print ("After Search======")
#     title2 = driver.title
#     print (title2)
#     time.sleep(2)
#     nowUrl2 = driver.current_url
#     print ("nowUrl2=" + nowUrl2)
#     time.sleep(2)
#     user = driver.find_element_by_class_name("nums").text
#     print (u"user数目=" + user)




time.sleep(5)
driver.quit()
