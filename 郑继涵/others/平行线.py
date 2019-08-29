import turtle
turtle.pensize(3)
turtle.pencolor("red")
for i in range(4):
    if i==1 or i==3:
        turtle.penup()
    else :
        turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
turtle.mainloop()