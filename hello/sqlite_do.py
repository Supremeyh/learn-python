#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据库
# 付费的商用数据库：Oracle，典型的高富帅；SQL Server，微软自家产品，Windows定制专款；DB2，IBM的产品，听起来挺高端；Sybase，曾经跟微软是好基友，后来关系破裂，现在家境惨淡。
# 免费的开源数据库：MySQL，大家都在用，一般错不了；PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；sqlite，嵌入式数据库，适合桌面和移动应用。

# SQLite,
# SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

# 表: 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
# Connection: 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# Cursor: 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。


# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库。 数据库文件是test.db, 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'sea\')')
# 通过rowcount获得插入的行数:
print(cursor.rowcount) # 1
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit() # 执行INSERT等操作后要调用commit()提交事务；
# 关闭Connection:
conn.close()

# 查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数
cursor.execute('select * from user where id=? and name=?', ('1', 'sea'))
# 获得查询结果集:
values = cursor.fetchall()
values # [('1', 'sea')]
print(values)
cursor.close()  # 确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露
conn.close()