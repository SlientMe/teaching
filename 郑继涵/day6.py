# -*- coding: utf-8 -*-
# @Time : 2019/7/23 18:50
# @Author : liuqi
# @FileName: day6.py
# @Software: PyCharm

'''

print(a.isalnum())
print(a.isdigit())
print(a.isalpha())

判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % (area))
else:
    print('不能构成三角形')



用户身份验证
username = input('请输入用户名: ')
password = input('请输入口令: ')
# 输入口令的时候终端中没有回显
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
'''