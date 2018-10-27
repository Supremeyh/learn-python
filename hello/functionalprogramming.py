# 面向过程的程序设计, 通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务。 函数就是面向过程的程序设计的基本单元

# 函数式编程, 一种抽象程度很高的编程范式 ，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# 高阶函数 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数。
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

# map 接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4])
L0 = list(r) # [1, 4, 9, 16] 


L1 = list(map(str, [1, 2, 3, 4, 5])) # 把list所有数字转为字符串



# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 对一个序列求和
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7]) # 16

# 把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def fn(x, y):
    return x * 10 + y

reduce(fn, [1, 3, 5, 7])


# 把str转换为int
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
    # return reduce(lambda x, y: x * 10 + y, map(char2num, s)) # 或用lambda函数进一步简化



# filter()函数用于过滤序列， 接收一个函数和一个序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# lsit删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))  # [1, 5, 9, 15]

# 用filter求素数 埃氏筛法
# 先构造一个从3开始的奇数序列
def _odd_iter():  # 一个生成器，并且是一个无限序列
    n = 1 
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > n

# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n 
        it = filter(_not_divisible(n), it) # 返回序列的第一个数

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else: 
            break


# sorted() 排序算法
sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]

# 接收一个key函数来实现自定义的排序
sorted([36, 5, -12, 9, -21], key=abs) # [5, 9, -12, -21, 36]

# 字符串排序 是按照ASCII的大小比较
# 忽略大小写的排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # ['about', 'bob', 'Credit', 'Zoo']

# 反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True) # ['Zoo', 'Credit', 'bob', 'about']




