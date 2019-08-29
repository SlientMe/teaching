# -*- coding: utf-8 -*-
# @Time : 2019/7/15 18:09
# @Author : liuqi
# @FileName: addthreading.py
# @Software: PyCharm

from time import ctime
import threading


def addme():
    sumResult = 0
    print(ctime())
    for i in range(99999999):
        sumResult += i
    print(sumResult)
    print(ctime())

# t = threading.Thread(target=addme(),name="add")
# t.start()   #6秒

addme()