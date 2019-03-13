# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/10 11:10
# @file：function_01.py
# @modified By:

from myProject.com.ZHENAI.encapsulation.encapsulation import UIHandle
from myProject.com.ZHENAI.constant.constant_01 import URL
from myProject.com.ZHENAI.config.config_01 import browser_config
from time import sleep


def option():
	driver = browser_config["chrome"]()
	uiHandle = UIHandle()
	uiHandle.init(driver)
	uiHandle.getUrl(URL)
	uiHandle.maxWindows()
	sleep(3)
	uiHandle.click(u"珍爱网首页", u"性别女")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"1996年")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"11月")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"22日")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"江西省")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"赣州市")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"南康区")
	sleep(1)
	uiHandle.click(u"珍爱网首页", u"注册按钮")
	sleep(1)
	uiHandle.close()


option()
