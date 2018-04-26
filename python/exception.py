#!/usr/bin/python3
import sys

'''
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    # j = i * (1/0)
# io异常
except OSError as err:
    print("OS error: {0}".format(err))
# 值转换异常
except ValueError:
    print("Could not convert data to an integer.")
# 其他异常
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
# 如果没有异常，还需要做的工作
else:
    print('Running ok, i is:', i)
print('\n--------------------------------------------------\n')
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
print('\n--------------------------------------------------\n')


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e.value)



def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide('2', '1')

for line in open("myfile.txt"):
    print(line, end="")
    print('\n--------------------------------------------------\n')
'''
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
