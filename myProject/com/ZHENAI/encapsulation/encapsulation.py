# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/10 10:06
# @file：encapsulation.py
# @modified By:

from myProject.com.ZHENAI.config.config_01 import location_config
from myProject.com.ZHENAI.log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIHandle():
	logger = Logger()

	@classmethod
	def init(cls, driver):
		cls.driver = driver

	@classmethod
	def getUrl(cls, url):
		cls.logger.loginfo(url)
		cls.driver.get(url)

	@classmethod
	def maxWindows(cls):
		cls.driver.maximize_window()

	@classmethod
	def close(cls):
		cls.driver.quit()

	@classmethod
	def element(cls, page, element):
		cls.logger.loginfo(page)
		e = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(location_config[page][element]))
		cls.logger.loginfo(page + "OK")
		return e

	@classmethod
	def elements(cls, page, element):
		cls.logger.loginfo(page)
		WebDriverWait(cls.driver, 10)
		es = cls.driver.find_elements(*location_config[page][element])
		return es

	@classmethod
	def input(cls, page, element, msg):
		es = cls.element(page, element)
		es.send_keys(msg)

	@classmethod
	def click(cls, page, element):
		es = cls.element(page, element)
		es.click()
