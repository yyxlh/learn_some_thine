#!/usr/bin/python
import re

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print('\n--------------------------------------------------\n')
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
print('\n--------------------------------------------------\n')
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

print('\n--------------------------------------------------\n')


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print('\n--------------------------------------------------\n')

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象
print(m.group(0))  # 可省略 0
print(m.start(0))  # 可省略 0
print(m.end(0))  # 可省略 0
print(m.span(0))  # 可省略 0

print('\n--------------------------------------------------\n')
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

print(re.split('\W+', 'runoob, runoob, runoob.'))   #不包含分隔符
print(re.split('(\W+)', ' runoob, runoob, runoob.')) #包含分隔符
print(re.split('\W+', ' runoob, runoob, runoob.', 1)) #分隔1次
print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
