# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2018/12/12 20:48
# @file：test01.py
# @modified By:
import unittest
import time


class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("开始测试")

	@classmethod
	def tearDownClass(cls):
		print("结束测试")

	def test01(self):
		print("执行测试用例test01")


if __name__ == '__main__':
	unittest.main
