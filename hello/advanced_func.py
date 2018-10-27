#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
L1 = list(range(100))
s = L1[0:10:2] # 取前0-10个数，每隔2个取一次
print(s)


# 迭代
# 判断一个对象是可迭代对象，通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('ABC', Iterable) # true, str可迭代

# enumerate函数可以把一个list变成索引-元素对
for k,v in enumerate(['a', 'b', 'c']): 
    print(k, v)


# 列表生成式
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 方法一 循环
L2 = list(range(1, 11)) 
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L3 = []
for x in range(1, 11):
    L3.append(x * x)
# 方法二 列表生成式
L4 = [x * x for x in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 筛选出仅偶数的平方
L5 = [x * x for x in range(1, 11) if x % 2 == 0] # [4, 16, 36, 64, 100]
# 两层循环 全排列
L6 = [m + n for m in 'ABC' for n in 'XYZ'] # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

dict6 = {'x': 'A', 'y': 'B', 'z': 'C' } #dict的items()可以同时迭代key和value
L7 = [k + ':' + v for k, v in dict6.items()]

 # 列出当前目录下的所有文件和目录名
import os
L8 = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

# 把一个list中所有的字符串变成小写
L9 = ['Hello', 'World', 'IBM', 'Apple']
L10 = [s.lower() for s in L9]


# generator 生成器
# 只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

next(g) # 不断执行 next()函数获得generator的下一个返回值，执行到最后一个元素时抛出StopIteration的错误

for n in g: # 或者用循环获得
    print(n)

# 斐波拉契数列（Fibonacci），即 除第一个和第二个数外，任意一个数都可由前两个数相加得到， 1, 1, 2, 3, 5, 8, 13, 21, ...
def fib(max):
    n, a, b = 0, 0 ,1
    while n < max:
        print(b)
        # yield b  # 把上述fib函数变成generator, 只需要把print(b)改为yield b就可以了
        # 定义generator的另一种方法,如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'

# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回,
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


# 捕获StopIteration错误  用for循环调用generator时，拿不到generator的return语句的返回值
g = fib(6) # 调用generator时,先生成一个generator对象
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break



# 可迭代对象Iterable  可以直接作用于for循环的对象统称为可迭代对象. 
# 一类是集合数据类型，如list、tuple、dict、set、str等，一类是generator，包括生成器和带yield的generator function
# 使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
isinstance((), Iterable) # True

# 迭代器Iterator  可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
isinstance((x for x in range(10)), Iterator) # True

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter('abc'), Iterator)

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：





