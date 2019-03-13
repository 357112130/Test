# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/10 11:22
# @file：test_01.py
# @modified By:

import unittest
from myProject.com.ZHENAI.function.function_01 import *


class test_case(unittest.TestCase):
	def setUp(self):
		pass

	def test_01(self):
		option()

	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main