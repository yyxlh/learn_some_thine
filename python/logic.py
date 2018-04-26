#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import math

r = 15
print('半径为%s的圆的面积：%.2f' % (r, (math.pi * r ** 2)))
print('半径为', r, '的圆的面积为：', (math.pi * r ** 2))

x, y, z = 1, 2, 3
print(x, y, z)
print(x)
print(y)

x, y = y, x
print(x, y, z)

student = {'小萌': '1001', '小强': '1002'}
key, value = student.popitem()
print(key)
print(value)
key, value = student.popitem()
print(key)
print(value)

field = 'hello,'
field += 'world'
print(field)
field *= 2
print(field)

x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)
print('---------------------')

print([1, 2] < [2, 1])
print([1, 2] < [1, 2])
print([1, 2] == [1, 2])
print([2, [1, 2]] < [2, [1, 3]])

x = 3
assert x > 0, "x is not zero or negative"
print('---------------------')
n = 1
while n <= 2:
    print('当前的数字是：', n)
    print('当前的数字是：', n)
    print('当前的数字是：', n)
    n += 1

fields = ['a', 'b', 'c']
for f in fields:
    print('当前的字母是:', f)

num = 0
while num < 3:
    print(num, '小于3')
    num += 1
else:
    print(num, '大于3')
    print('循环结束\n')
print('\n---------------------\n')
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
print('\n---------------------\n')
for i in range(5):
    print(i)
print('\n---------------------\n')
for i in range(5, 9):
    print(i)
print('\n---------------------\n')
for i in range(0, 10, 3):
    print(i)

print('\n---------------------\n')
import random
while n < 1000:
    a=random.randint(1,9)
    b=random.randint(1,9)
    print(a,' + ',b,' = ____')
    n +=1