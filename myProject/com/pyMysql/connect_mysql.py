# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/21 10:20
# @File: connect_mysql.py
# @Description: connect mysql
# @Modified By: ycg

import pymysql as db
import sys
import traceback

config = {
	"host": "127.0.0.1",  # localhost本地地址
	"port": 3306,  # 端口号
	"user": "root",  # 用户名
	"passwd": "root",  # 密码
	"database": "test",  # 数据库
	"charset": "utf8",  # 编码格式
	"cursorclass": db.cursors.DictCursor  # 自定义光标类使用
}

# 连接数据库
try:
	conn = db.connect(**config)
	conn.autocommit(1)
	cursor = conn.cursor()
except IOError, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

# 创建数据库
try:
	DB_NAME = "test"
	cursor.execute("DROP DATABASE IF EXISTS %s" % DB_NAME)
	cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % DB_NAME)
	conn.select_db(DB_NAME)

	# 创建表
	TABLE_NAME = "user"
	TABLE_NAME1 = "user1"
	cursor.execute("CREATE TABLE %s(id int primary key,name varchar(30))" % TABLE_NAME)
	cursor.execute("CREATE TABLE %s(id int primary key,name varchar(30))" % TABLE_NAME1)

	# 删除表
	cursor.execute("DROP TABLE %s" % TABLE_NAME1)

	# 批量插入纪录
	values = []
	for i in range(10):
		values.append((i, "n" + str(i)))
	cursor.executemany("INSERT INTO user values(%s,%s)", values)

	# 查询数据条目
	count = cursor.execute("SELECT * FROM %s" % TABLE_NAME)
	print "total records:", cursor.rowcount

	# 获取表名信息
	desc = cursor.description
	print "%s %3s" % (desc[0][0], desc[1][0])

	cursor.scroll(0, mode="absolute")
	results = cursor.fetchall()
	for result in results:
		print result

except IOError, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)
	traceback.print_exc()
	# 发生错误时会滚
	conn.rollback()
finally:
	# 关闭游标连接
	cursor.close()
	# 关闭数据库连接
	conn.close()
