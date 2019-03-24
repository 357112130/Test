import pymysql as db
import sys

# install mysqlclient
db.install_as_MySQLdb()

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
	conn.autocommit(1)
	cursor = conn.cursor()

	# 查看数据库版本
	sql_version = "SELECT VERSION()"
	cursor.execute(sql_version)
	data = cursor.fetchone()
	print("数据库版本: %s" % data)
# 异常打印log
except IOError as e:
	print("Error %d: %s" % (e.args[0], e.args[1]))
	sys.exit(1)
# 断开数据库连接
finally:
	cursor.close()
	conn.close()
