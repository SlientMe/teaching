# -*- coding: utf-8 -*-
# @Time : 2019/7/21 9:59
# @Author : liuqi
# @FileName: day10.py
# @Software: PyCharm

# 猜字游戏

import random
x = random.randint(0, 99)
while(True):
    num = input("请猜猜是多少")
    if(num.isdigit()):
        num = int(num)
        if(x == num):
            print("恭喜你，猜对了")
            break
        elif(x>num):
            print("你猜小了")
        elif(x<num):
            print("你猜大了")