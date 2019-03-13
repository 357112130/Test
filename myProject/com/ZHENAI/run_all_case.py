# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 用来执行所有用例
# @date: create in 2019/3/10 9:44
# @file：run_all_case.py
# @modified By:

import unittest
import HTMLTestRunner
import time


def createSuit(lists):
	testcase = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(lists, pattern="test*.py", top_level_dir=None)
	for test_suit in discover:
		for test_case in test_suit:
			testcase.addTests(test_case)
			print(testcase)
	return testcase


list_01 = "D://pyProject//myProject//com//ZHENAI//test_case//"
all_case = createSuit(list_01)
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = "D://pyProject//myProject//com//ZHENAI//report//" + now + "result.html"
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Test测试", description=u"用例执行情况")
runner.run(all_case)
fp.close()

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
