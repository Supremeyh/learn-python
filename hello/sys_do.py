#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'sea' # 特殊变量

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello, python')
    elif len(args)==2:
        print('hello, %s' % args[1]) # args[0]为第一个参数永远是该.py文件的名称
    else:
        print('too many arguments')

    
if __name__ == '__main__':
    test()

# 当我们在命令行运行本sys模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该sys模块时， if判断将失败.
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。