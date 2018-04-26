# !/usr/bin/python3
# -*- coding: UTF-8 -*-

def func():
    a = 10
    b = 20
    print(a)
    print(b)
    print('a+b的和是：', a + b)


func()


###############################################
def personinfo(arg, *vartuple):
    print(arg)
    for var in vartuple:
        print(var)
    return


print('-------------------')
personinfo('小萌')
print('-------------------')
personinfo('小萌', '北京', 123, 'abc')

other = {'城市': '北京', '爱好': '编程'}


def personinfo(name, number, **kw):
    print('姓名：', name, '学号：', '其他：', kw)


personinfo('小智', 1002, 城市=other['城市'], 爱好=other['爱好'])
personinfo('小智', 1002, **other)


###############################################
def exp(p1, p2, df=0, *vart, **kw):
    print('p1=', p1, 'p2=', p2, 'df=', df, 'vart=', vart, 'kw=', kw)


exp(1, 2)
exp(1, 2, c=3)
exp(1, 2, 3, 'a', 'b')
exp(1, 2, 3, 'abc', x=9)

args = (1, 2, 3, 4)  # 定义tuple
kw = {'x': 8, 'y': 9}  # 定义dict
exp(*args, **kw)


###############################################
def sum_late(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return calc_sum


print('调用sum_late的结果：', sum_late(1, 2, 3, 4))
sum1 = sum_late(1, 2, 3, 4)  # 类似于函数指针
print('调用calc_sum之后的结果：', sum1)
print('调用calc_sum之后的结果：', sum1())


###############################################
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('递归调用：', fact(5))


# print('递归调用：',fact(1000))
###############################################
def func(x):
    return x > 3


f_list = filter(func, [1, 2, 3, 4, 5, 6])
print('列表中大于3的元素有：', [item for item in f_list])

print('列表中大于3的元素有：', [item for item in filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6, 7])])
###############################################
from functools import partial


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print('自定义函数，100对7取余：', mod(100, 7))
print('偏函数，100对7取余：', mod_by_100(7))
