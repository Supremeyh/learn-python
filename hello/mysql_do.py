#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MySQL

# MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
# 而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。
# 由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。

# 安装MySQL
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
# 安装命令
# pip install mysql-connector-python --allow-external mysql-connector-python
# pip install mysql-connector  


# change root password to yours:

# 连接到MySQL服务器的test数据库
# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='password', datebase='test')
cursor = conn.cursor()
# 创建user表:
cursor.excute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.excute('insert into user (id, name) values (%s, %s)', ['1', 'sea'])
print('rowcount = ', cursor.rowcount) # 1
# 提交事务:
cursor.commit()
cursor.close()


# 运行查询:
cursor = conn.cursor()
cursor.excute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values # [('1', 'sea')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()










