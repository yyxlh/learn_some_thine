#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import this

'''
#print('hello world!\nyangyu')
print('hello world!\n%s\n%d' % ('yangyu', 2018))

print('Pi is %+010.2f' % 3.1415926)

num=[1,2,3,4,5]
#print('连接：','+'.join(num))
str=['1','2','3','4','5']
mask='+'
print('连接：',mask.join(str))

print('\n---------------------\n')
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

print('\n---------------------\n')
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

print('\n---------------------\n')
import sys

'''
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

# !/usr/bin/python3
import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')


