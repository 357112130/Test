# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: ycg
# @description: 
# @date: create in 2019/3/24 15:07
# @file：mysql_helper.py
# @modified By:
import pymysql as db


class MysqlHelper:
	def __init__(self, host, port, user, password, database, charset):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.database = database
		self.charset = charset
		self.db = None
		self.cursor = db.cursors.DictCursor

	# 数据库连接
	def open(self):
		self.db = db.connect(host=self.host, port=self.port, user=self.user, password=self.password,
							 database=self.database, charset=self.charset)
		self.cursor = self.db.cursor()

	# 数据库关闭
	def close(self):
		self.cursor.close()
		self.db.close()

	# 数据增删改
	def cud(self, sql, params):
		self.open()
		try:
			self.cursor.execute(sql, params)
			self.db.commit()
			print("ok")
		except:
			print('cud出现错误')
			self.db.rollback()
		self.close()

	# 数据查询
	def find(self, sql, params):
		self.open()
		try:
			result = self.cursor.execute(sql, params)
			self.close()
			print("ok")
			return result
		except:
			print('find出现错误')
