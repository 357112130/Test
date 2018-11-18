# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: ycg
# @Date: 2018/10/21 10:20
# @File: connect_mysql.py
# @Description: connect mysql
# @Modified By: ycg

import pymysql as db
import sys
import traceback  # 回滚

# 数据库配置
config = {
	"host": "127.0.0.1",  # localhost本地地址
	"port": 3306,  # 端口号
	"user": "root",  # 用户名
	"passwd": "root",  # 密码
	"database": "test",  # 数据库
	"charset": "utf8",  # 编码格式
	"cursorclass": db.cursors.DictCursor  # 自定义光标类使用
}

try:
	# 连接数据库
	conn = db.connect(**config)
	conn.autocommit(1)
	cursor = conn.cursor()
except IOError, e:
	# 打印error log
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

try:
	# 创建数据库
	DB_NAME = "test"
	cursor.execute("drop database if exists %s" % DB_NAME)
	cursor.execute("create database if not exists %s" % DB_NAME)
	conn.select_db(DB_NAME)

	# 创建表
	TABLE_NAME = "user"
	cursor.execute("create table %s(id int primary key,name varchar(30))" % TABLE_NAME)

	# 删除表
	if DB_NAME == 1:
		cursor.execute("drop table %s" % TABLE_NAME)
	pass

	# 批量插入数据
	values = []
	for i in range(21):
		values.append((i, "n" + str(i)))
	cursor.executemany("insert into user values(%s,%s)", values)

	# 查询表数据条目
	count = cursor.execute("select * from %s" % TABLE_NAME)
	print "total records:(总记录)", cursor.rowcount

	# 获取表名信息
	desc = cursor.description
	print "%s %3s" % (desc[0][0], desc[1][0])

	cursor.scroll(0, mode="absolute")
	results = cursor.fetchall()
	for result in results:
		print result

except IOError, e:
	# 打印error log
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)
	traceback.print_exc()
	# 发生错误时回滚
	conn.rollback()
finally:
	# 关闭游标连接
	cursor.close()
	# 关闭数据库连接
	conn.close()
