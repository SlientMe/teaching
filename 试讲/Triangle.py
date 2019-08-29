import turtle
turtle.setup(600,600)
size=20
turtle.pensize(size)
turtle.color("red")
length= 200
turtle.fd(length)
turtle.left(120)
turtle.fd(length)
turtle.seth(240)  # 这里等于left(120) seth总是以向东的方向为起点
turtle.fd(length)