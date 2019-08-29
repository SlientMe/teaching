import turtle
import random
turtle.speed(0)
turtle.bgcolor("black")
turtle.width(5)
s = ["唱","跳","rap","篮球","鸡你太美"]
for y in range(100):
    turtle.penup()
    turtle.goto(random.randint(-350, 350),random.randint(-350, 350))
    turtle.pendown()
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)
    for x in range(1):
        turtle.write(s[random.randint(0,4)],font=('arial',18,'normal'))
        turtle.left(144)
turtle.done()
