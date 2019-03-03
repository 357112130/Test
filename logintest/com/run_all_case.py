# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/2 18:23
# @file：run_all_case.py
# @modified By:
import unittest
import os
import HTMLTestRunner
from logintest.com.send_email import mains
from BeautifulReport import BeautifulReport


# 待执行用例的目录
def allcase():
	case_dir = "D://pyProject//logintest//com//testcase//logintest"
	# case_path=os.path.join(os.getcwd(),"case")
	testcase = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
	# discover方法筛选出来的用例，循环添加到测试套件中
	for test_suite in discover:
		for test_case in test_suite:
			# 添加用例到testcase
			print(test_case)
			testcase.addTest(test_case)
	return testcase


if __name__ == "__main__":
	# runner=unittest.TextTestRunner()
	# runner.run(allcase())
	report_path = "D://pyProject//logintest//com//testcase//report_test//result_logintest.html"
	fp = open(report_path, "wb")
	# runner = BeautifulReport(allcase())
	# runner.report_test(description=u"test报告",filename=u"自动化测试unittest测试框架报告")
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试unittest测试框架报告", description=u"用例执行情况:")
	runner.run(allcase())
	fp.close()

	# 发送测试报告邮件
	mains()
