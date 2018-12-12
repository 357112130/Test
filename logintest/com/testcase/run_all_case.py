# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2018/12/12 20:08
# @file：run_all_case.py
# @modified By:
import unittest
import os
import HtmlTestRunner
from send_email import main2


# 待执行用例的目录
def allcase():
	case_dir = r"D:\pyProject\logintest\com\testcase"
	# case_path=os.path.join(os.getcwd(),"case")
	testcase = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
	# discover方法筛选出来的用例，循环添加到测试套件中
	# print(discover)
	for test_suite in discover:
		for test_case in test_suite:
			# 添加用例到testcase
			print(test_case)
		testcase.addTest(test_case)
	return testcase


if __name__ == "__main__":
	# runner=unittest.TextTestRunner()
	# runner.run(allcase())
	report_path = "D://pyProject//logintest//com//testcase//result.html"
	fp = open(report_path, "wb")
	runner = HtmlTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
	runner.run(allcase())
	fp.close()
# main2()  #from send_email import main2  发送邮件！
