# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description:
# @date: create in 2019/3/3 15:19
# @file：run_case.py
# @modified By:
import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner
from myProject.com.appiumTest.data.data import report_data

test_dir = "./testcase"
discover = unittest.defaultTestLoader.discover(start_dir="./testcase", pattern="test*.py")

if __name__ == "__main__":
	report_dir = "./test_report"
	os.makedirs(report_dir, exist_ok=True)
	now = time.strftime("%Y-%m-%d %H-%M-%S")
	report_name = "{0}/{1}.html".format(report_dir, now)

	with open(report_name, "wb")as f:
		runner = HTMLTestRunner(stream=f, title=report_data["title"], description=report_data["desc"])
		runner.run(discover)
		f.close()
