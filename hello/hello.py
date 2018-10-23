#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('hello python')

birth = input('birth: ')
age = int(birth)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teen')
else:
    print('kid')
