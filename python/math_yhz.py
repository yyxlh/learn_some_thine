#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import random

total_cnt = 48
max_num=9

print('\n----------     less than ten + or -     -----------\n')
one_num = {' 1 +  1 =  2': '0'}

for i in range(0, 5000):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    if a + b < 20:
        one_num['%2d + %2d = __' % (a, b)] = '1'
    if one_num.__len__() > total_cnt * 1:
        break
print(one_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    if a > b:
        one_num['%2d + __ = %2d' % (b, a)] = '1'
    if one_num.__len__() > total_cnt * 2:
        break
print(one_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    if a > b:
        one_num['__ + %2d = %2d' % (b, a)] = '1'
    if one_num.__len__() > total_cnt * 3:
        break
print(one_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    if a > b:
        one_num['%2d - __ = %2d' % (a, b)] = '1'
    if one_num.__len__() > total_cnt * 4:
        break
print(one_num.__len__())

f = open('./out/one_num.txt', 'w')
it = iter(one_num)
for x in it:
    print('%s' % x)
    f.write('%s\n' % x)
f.close()

print('\n----------     two number + or -     -----------\n')
two_num = {' 1 +  1 =  2': '0'}
for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    if a + b < 20:
        two_num['%2d + %2d = __' % (a, b)] = '1'
    if two_num.__len__() > total_cnt * 1:
        break
print(two_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    if a > b:
        two_num['%2d + __ = %2d' % (b, a)] = '1'
    if two_num.__len__() > total_cnt * 2:
        break
print(two_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    if a > b:
        two_num['__ + %2d = %2d' % (b, a)] = '1'
    if two_num.__len__() > total_cnt * 3:
        break
print(two_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    if a > b:
        two_num['%2d - __ = %2d' % (a, b)] = '1'
    if two_num.__len__() > total_cnt * 4:
        break
print(two_num.__len__())

f = open('./out/two_num.txt', 'w')
it = iter(two_num)
for x in it:
    print('%s' % x)
    f.write('%s\n' % x)
f.close()

print('\n----------     three number + or -     -----------\n')
three_num = {' 1 +  1 + 1 =  3': '0'}
for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    c = random.randint(1, 19)
    if a + b + c < 20:
        three_num['%2d + %2d + %2d = __' % (a, b, c)] = '1'
    if three_num.__len__() > total_cnt * 1:
        break
print(three_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    c = random.randint(1, 19)
    if a > b + c:
        three_num['%2d + %2d + __ = %2d' % (b, c, a)] = '1'
    if three_num.__len__() > total_cnt * 2:
        break
print(three_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    c = random.randint(1, 19)
    if a > b + c:
        three_num['%2d - %2d - %2d = __' % (a, b, c)] = '1'
    if three_num.__len__() > total_cnt * 3:
        break
print(three_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 19)
    b = random.randint(1, 19)
    c = random.randint(1, 19)
    if a - b + c > 0:
        three_num['%2d - %2d + %2d = __' % (a, b, c)] = '1'
    if three_num.__len__() > total_cnt * 4:
        break
print(three_num.__len__())

f = open('./out/three_num.txt', 'w')
it = iter(three_num)
for x in it:
    print('%s' % x)
    f.write('%s\n' % x)
f.close()

print('\n----------     four number + or -     -----------\n')
four_num = {' 1 +  1 + 1 + 1 =  4': '0'}
for i in range(0, 5000):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    if a + b + c + d < 20:
        four_num['%2d + %2d + %2d + %2d = __' % (a, b, c, d)] = '1'
    if four_num.__len__() > total_cnt * 1:
        break
print(four_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    if a + b > c + d:
        four_num['(%2d + %2d)-(%2d + %2d) = __' % (a, b, c, d)] = '1'
    if four_num.__len__() > total_cnt * 2:
        break
print(four_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    if a > b and c > d:
        four_num['(%2d - %2d)+(%2d - %2d) = __' % (a, b, c, d)] = '1'
    if four_num.__len__() > total_cnt * 3:
        break
print(four_num.__len__())

for i in range(0, 5000):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    if a > b and c > d and a - b > c - d:
        four_num['(%2d - %2d)-(%2d - %2d) = __' % (a, b, c, d)] = '1'
    if four_num.__len__() > total_cnt * 4:
        break
print(four_num.__len__())

f = open('./out/four_num.txt', 'w')
it = iter(four_num)
for x in it:
    print('%s' % x)
    f.write('%s\n' % x)
f.close()
