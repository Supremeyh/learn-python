# IO编程
# IO在计算机中指Input/Output，也就是输入和输出。
# IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
# Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
# CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题：同步IO；异步IO
# 操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用。
# 现代操作系统不允许普通的程序直接操作磁盘，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读文件

# 读文件
try:
  f = open('/Users/sea/test.txt', 'r')
  f.read()
finally:
  if f:
    f.close()

# 使用with语句操作文件IO是个好习惯。
with open('/path/to/file', 'rb') as f:  # 二进制文件 rb
    print(f.read())


# 字符编码 
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 读文件
f = open('/Users/michael/test.txt', 'w')   # 二进制文件 wb
f.write('Hello, world!')
f.close()



# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

# 操作文件和目录 os
import os  # Python内置的os模块也可以直接调用操作系统提供的接口函数
# 操作系统类型, 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
os.name()
# 操作系统详细信息 window系统不生效
os.uname() 
# 环境变量
os.environ()
# 查看当前目录的绝对路径
os.path.abspath('.')
# 路径合成 os.path.join()
os.path.join('/Users/sea/Desktop/OnGoing', 'cars')  # '/Users/sea/Desktop/OnGoing/cars'
# 拆分路径 os.path.split()
os.path.split('/Users/michael/testdir/file.txt')  # ('/Users/michael/testdir', 'file.txt')
# 在某个目录下创建一个新目录
os.path.join('/Users/sea/Desktop/OnGoing', 'cars')
os.mkdir('/Users/sea/Desktop/OnGoing/testdir')
# 在某个目录下删除一个目录
os.rmdir('/Users/sea/Desktop/OnGoing/testdir')
# 对文件重命名
os.rename('test.txt', 'test.py')
# 删掉文件
os.remove('test.py')

# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
# 要列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



# 序列化，pickling 或 serialization， 把变量从内存中变成可存储或传输的过程称之为序列化
# pickle模块来实现序列化
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d) # 序列化成一个bytes
pickle.dump(d) # 序列化成一个file-like Object

f = open('dump.txt', 'rb')
d = pickle.load(f) # 反序列化出对象

# JSON
import json
d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
json.dumps(d) # '{"age": 20, "score": 88, "name": "Bob"}'
# 把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.load(json_str) # {'age': 20, 'score': 88, 'name': 'Bob'}






