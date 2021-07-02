## 通过Python与数据库进行交互


import pymysql

# 连接数据库
# 填入连接数据库的账号密码
conn = pymysql.connect(host="",
						port=3306,
						user="admin",
						password="admin")
						
# 创建游标，并返回字典类型数据
cursor = conn.cursor(pymysql.cursor.DictCursor)

# 操作数据库
sql = "SHOW DATABASES;"
nums = cursor.execute(sql)
data = cursor.fetchall()
for item in data:
	print(item)

# 关闭数据库
cursor.close()
conn.close()