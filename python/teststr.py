#!/usr/bin/python3
# -*- coding: UTF-8 -*-

intab = 'adfas'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
st = 'just do it'
print('st translate 后：', st.translate(trantab))

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict1['Name']: ", dict1['Name'])
print("dict1['Age']: ", dict1['Age'])

student = [('name', '小萌'), ('number', '1001')]
detail = dict(student)
print('学生信息：', detail)

student1 = {'小萌': '1001', '小强': '1002'}
print('小强的学号 %(小强)s' % student1)
print('小强的学号 %s' % student1['小强'])
student1['小强'] = '1005'
print('小强的学号 %(小强)s' % student1)
student1['小张'] = '1006'
print('小张的学号 %(小张)s' % student1)
