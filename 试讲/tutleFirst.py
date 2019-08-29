# -*- coding: utf-8 -*-
# @Time : 2019/7/12 21:14
# @Author : liuqi
# @FileName: tutleFirst.py
# @Software: PyCharm

# import turtle完成库的引用  也可以用from turtle import*的形式，这种方式可以直接使用函数，但会出现重名问题,也可以使用import turtle as 别名   这种方法最好
import turtle

turtle.setup(650, 350)     #启动窗体的位置和大小
turtle.penup()            #抬起画笔
turtle.fd(-250)
turtle.pendown()          #落下画笔
turtle.pensize(20)        #画笔宽度
turtle.pencolor("purple") #修改画笔颜色，也可以用这种方式turtle.pencolor(1,1,1)
turtle.right(50)          # 改变海龟的行进方向，不行进

for i in range(4):
    turtle.circle(50, 100)  # circle(r,angle) 以海龟左侧的某个点为圆心进行曲线运行 ，r为负数则为右侧
    turtle.circle(-50, 100)
# turtle.circle(50,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)
turtle.done()            #用来停止画笔绘制，但绘图窗体不关闭