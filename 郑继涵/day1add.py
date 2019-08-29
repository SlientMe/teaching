import turtle

turtle.setup(650, 650)  #启动窗体的位置和大小
turtle.pensize(5)        #画笔宽度
turtle.pencolor("red")  #修改画笔颜色，也可以用这种方式turtle.pencolor(1,1,1)
turtle.speed(1)           #画笔的速度
turtle.penup()
turtle.forward(-100)
turtle.pendown()

# turtle.fillcolor("red")
# turtle.begin_fill()

turtle.forward(200)    #让海龟先前进200px
turtle.right(144)   # 改变海龟的行进方向，不行进
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)


# turtle.end_fill()

turtle.mainloop()

# turtle.seth(240)  # 这里等于left(120) seth总是以向东的方向为起点
