#!/usr/bin/python3

import time;  # 引入time模块

'''
ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


import calendar

cal = calendar.month(2018, 1)
print ("以下输出2018年1月份的日历:")
print (cal)


def procedure():
    time.sleep(2.5)

# time.clock
t0 = time.clock()
procedure()
print (time.clock() - t0)

# time.time
t0 = time.time()
procedure()
print (time.time() - t0)

t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print ("time.mktime(t) : %f" %  secs)

import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))
'''

from datetime import datetime, date, time

# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))

# Using datetime.now() or datetime.utcnow()
print(datetime.now())
print(datetime.utcnow())

# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)

# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:
    print(it)
print('\n--------------------------------------------------\n')
# Date in ISO format
ic = dt.isocalendar()
for it in ic:
    print(it)
# Formatting datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time"))

