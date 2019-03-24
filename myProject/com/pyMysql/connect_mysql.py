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
	"password": "root",  # 密码
	"database": "test",  # 数据库名
	"charset": "utf8",  # 编码格式
	"cursorclass": db.cursors.DictCursor  # 自定义光标类使用
}

# 连接数据库
try:
	conn = db.connect(**config)
	conn.autocommit(1)  # 自动提交
	cursor = conn.cursor()
	print("数据库连接成功...")
# 异常 打印error log
except IOError as e:
	print("Error %d: %s" % (e.args[0], e.args[1]))
	sys.exit(1)

# 查看数据库版本
sql_version = "SELECT VERSION()"
cursor.execute(sql_version)
data = cursor.fetchone()
print("数据库版本: %s" % data)

# 操作数据库
try:
	# 创建数据库
	DB_NAME = "test"
	cursor.execute("drop database if exists %s" % DB_NAME)
	cursor.execute("create database if not exists %s" % DB_NAME)

	# 选择数据库
	conn.select_db(DB_NAME)

	# 创建表
	TABLE_NAME = "user"
	sql_create = "create table %s(id int primary key not null," \
				 "name varchar(30) not null comment '姓名'," \
				 "age varchar(30) not null comment '年龄'," \
				 "sex varchar(30) not null comment '性别'," \
				 "id_card varchar (255) not null comment '身份证'," \
				 "tel_number varchar(255) default null comment '电话'," \
				 "email varchar(255) default null comment '邮箱'," \
				 "address varchar(255) default null comment '地址')" % TABLE_NAME
	cursor.execute(sql_create)

	# 删除表
	if DB_NAME == "":
		cursor.execute("drop table %s" % TABLE_NAME)

	# 批量插入数据
	values = []
	for i in range(0, 100):
		values.append((i, "name" + str(i), "age" + str(i), "sex" + str(i), "icard" + str(i), "tel" + str(i),
					   "email" + str(i), "address" + str(i)))
	cursor.executemany("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)", values)

	# 修改数据
	sql_update = "update user set name = 'ycg' where id = '0' "
	cursor.execute(sql_update)

	# 删除数据
	sql_delete = "delete from user where id = '1' "
	cursor.execute(sql_delete)

	# 查询表数据条目
	count = cursor.execute("select * from %s" % TABLE_NAME)
	print("total records(总记录):", cursor.rowcount)

	# 获取表名信息
	desc = cursor.description
	print("field_name(字段名):" + "%s %3s %3s %3s %4s %3s %5s %6s" % (
		desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0], desc[6][0], desc[7][0]))

	# 获取数据
	cursor.scroll(0, mode="absolute")
	results = cursor.fetchall()
	for result in results:
		print(result)

# 异常 打印error log
except IOError as e:
	print("Error %d: %s" % (e.args[0], e.args[1]))
	sys.exit(1)
	traceback.print_exc()
	# 发生错误时回滚
	conn.rollback()
	print("数据库异常,回滚!")

# 关闭数据库
finally:
	# 关闭游标连接
	cursor.close()
	# 关闭数据库连接
	conn.close()
	print("数据库已断开连接...")
