import turtle
turtle.pensize(3)
turtle.pencolor("red")
turtle.speed(9)
for i in range(100):
    turtle.pencolor(i/100, i/100, i/100)
    for j in range(4):
        if j == 1:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(i)
        turtle.left(90)
turtle.mainloop()
