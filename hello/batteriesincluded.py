# 常用内建模块

# datetime是Python处理日期和时间的标准库。
from datetime import datetime
now = datetime.now() # 当前datetime 
print(now) # 2018-11-09 23:18:43.058269
print(type(now)) # 类型是datetime

# 获取指定日期和时间
dt = datetime(2018, 11, 9, 23, 20) # 用指定日期时间创建datetime
print(dt)  # 2018-11-09 23:20:00


# timestamp
# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数）
# 当前时间就是相对于epoch time的秒数，称为timestamp
# 格林威治标准时间 timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00， 对应北京时间是：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


# datetime转换为timestamp
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
dt1 = datetime(2018, 11, 9, 23, 24)
dt.timestamp() # 1541776800.0  
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。


# timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t2 = 1541776800.0  
dt2 = datetime.fromtimestamp(t2) # 本地时间 2018-11-09 23:20:00
dt3 = datetime.utcfromtimestamp(t2) # UTC时间 2018-11-09 15:20:00
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。


# str转换为datetime
# 通过datetime.strptime(), 注意转换后的datetime是没有时区信息的。
cday = datetime.strptime('2018-11-9 23:37:10', '%Y-%m-%d %H:%M:%S')  # 2018-11-09 23:37:10

# datetime转换为str
# 通过strftime()
now2 = datetime.now()
str = now2.strftime('%a, %b %d %H:%M')  # Fri, Nov 09 23:40


# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import datetime, timedelta
now = datetime.now()
now + timedelta(days=2, hours=12) 
# 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。


# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now3 = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00














