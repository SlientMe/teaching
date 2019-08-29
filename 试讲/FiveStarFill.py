# -*- coding: utf-8 -*-
# @Time : 2019/7/13 0:06
# @Author : liuqi
# @FileName: FiveStarFill.py
# @Software: PyCharm
import turtle

turtle.pensize(10)
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.fd(200)
    turtle.right(144)
turtle.end_fill()
turtle.done()