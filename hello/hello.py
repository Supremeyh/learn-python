#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# hello python
print('hello python')


# if
birth = input('birth: ')
age = int(birth)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teen')
else:
    print('kid')


# for 循环
# 计算1-100的整数之和
s = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
for x in list(range(101)):
    s = s + x
print(s)

# while 循环
# 计算100以内所有奇数之和
s1 = 0
n = 99
while n > 0:
    s1 = s1 + n
    n = n - 2
print(s1)

# break 提前结束循环
# 打印1-10
n = 1
while n < 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END break')

# continue 提前结束本轮循环，并直接开始下一轮循环
# 打印1-10的奇数
m = 0
while m < 10:
    m = m + 1
    if m % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(m)


# dict
# dict和list相比是空间换时间
d = {'name': 'sea', 'age': 20}
'name' in d
d.get('age', 22)

# set
ss1 = set([1, 1, 3, 5])
ss2 = set([2, 3, 4])
print(ss1 & ss2)
print(ss1 | ss2)